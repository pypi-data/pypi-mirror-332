import httpx
import multiprocessing
from multiprocessing import Queue
import time 
import hashlib 
import atexit
from io import StringIO
import ase.io
from openmm import unit
import ase.io
from io import StringIO
import json 
import os 
import random 

__version__ = '0.1.14'

# Linux/Mac/Windows compatible path. 
token_path = os.path.expanduser("~/.logmd_token")
dev = False
base_url = 'https://rcsb.ai' if not dev else 'http://localhost:5173'

# Conversion constants. 
eV_to_K = 11604.5250061657

class LogMD:
    def __init__(self, num_workers=3, project='', template='', interval=100):
        t0 = time.time()
        self.frame_num = 0
        self.interval = interval
        self.project = project
        self.token = None

        self.adjectives = adjectives
        self.nouns = nouns 
        self.logged_in = False 

        if template != '': self.template = ase.io.read(template) # for openmm

        # if no project => log publically, no need to log-in. 
        if self.project != '': 
            # if no token, try to setup token, then log-in (i.e. load token). 
            if not os.path.exists(token_path): 
                LogMD.setup_token()

            try:
                self.load_token() 
            except:
                print(f'\033[90m[\033[32mlogmd\033[90m] token file is corrupted, please login again')
                LogMD.setup_token()
                self.load_token()

        # Upload using multiple processes
        self.upload_queue = Queue()
        self.status_queue = Queue()
        self.num_workers = num_workers
        self.upload_processes = []
        
        for _ in range(self.num_workers):
            process = multiprocessing.Process(
                target=self.upload_worker_process,
                args=(self.upload_queue, self.status_queue, self.token, self.project)
            )
            process.start()
            self.upload_processes.append(process)
        
        self.num = self.num_files() + 1

        # If logged-in use <adjective><noun><num> as name. 
        if self.logged_in: 
            i, j = random.randint(0, len(self.adjectives) - 1), random.randint(0, len(self.nouns) - 1)
            self.run_id = f'{self.adjectives[i]}-{self.nouns[j]}-{self.num}'
            self.url = f'{base_url}/logmd/{self.project}/' + self.run_id
        # if not logged in, store publically, use sha256 hash to remove collision. 
        else: 
            # pr[collision]~1/16^10=1e-12
            # E[draws to get collision]~sqrt(pr[collision])~1e-5    (birthday paradox)
            # => we have to check...
            self.run_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:10]
            while httpx.head(f"https://logmd.b-cdn.net/public/{self.run_id}/").status_code == 200: 
                self.run_id = hashlib.sha256(str(time.time() + random.random()).encode()).hexdigest()[:10]
            self.url = f'{base_url}/logmd/' + self.run_id
        
        # Print init message with run id. 
        print(f'\033[90m[\033[32mlogmd\033[90m] \033[90mload_time=\033[34m{time.time()-t0:.2f}s\033[90m\033[0m ')
        print(f'\033[90m[\033[32mlogmd\033[90m] \033[90mid=\033[34m{self.run_id}\033[90m\033[0m 🚀')
        print(f'\033[90m[\033[32mlogmd\033[90m] \033[90murl=\033[34m{self.url}\033[90m\033[0m 🚀')
        
        # Cleanup asynch processes when python exists. 
        atexit.register(self.cleanup)

    def load_token(self):
        with open(token_path, 'r') as token_file: 
            self.token = json.load(token_file)
            self.logged_in = True

    @staticmethod
    def setup_token():
        print(f'\033[90m[\033[32mlogmd\033[90m] login here: \033[34m{base_url}/auth')
        token = input()
        with open(token_path, 'w') as token_file: 
            token_file.write(token)


    def cleanup(self):
        print(f'\033[90m[\033[32mlogmd\033[90m] finishing uploads (if >5s open issue https://github.com/log-md/logmd)')

        # Send termination signal to all worker processes
        for _ in range(self.num_workers):
            self.upload_queue.put(None)
        for process in self.upload_processes:
            process.join()
        print(f'\033[90m[\033[32mlogmd\033[90m] id=\033[34m{self.url}\033[0m ✅')

    @staticmethod
    def upload_worker_process(upload_queue: Queue, status_queue: Queue, token: dict, project: str):
        """Worker process that handles uploads"""
        client = httpx.Client(timeout=180)  
        
        while True:
            item = upload_queue.get()  
            if item is None:  break
            atom_string, frame_num, run_id, data_dict= item

            if dev: url = "https://alexander-mathiasen--logmd-upload-frame-dev.modal.run"
            else: url = "https://alexander-mathiasen--logmd-upload-frame.modal.run"

            data = {
                "user_id": "public" if token is None else token['email'],
                "run_id": run_id,
                "frame_num": str(frame_num),
                "file_contents": atom_string,
                "token": None if token is None else token['token'] ,
                "project": project,
                "data_dict": data_dict,  
            }

            response = client.post(url, json=data)
            status_queue.put((frame_num, response.status_code))
        
        client.close()

    # for openmm
    def describeNextReport(self, simulation):
        steps = self.interval 
        return (steps, True, True, True, False)
    # for openmm
    def report(self, simulation, state):
        """ Method openmm calls: simulation.reporters.append(LogMD(template='1crn.pdb', interval=100)). """
        self.template.positions = state.getPositions(asNumpy=True).value_in_unit(unit.angstrom) 
        self.__call__(self.template)

    # for ase 
    def __call__(self, atoms, dyn, data_dict={}):
        """Method ASE calls:  dyn.attach(logmd) """
        self.frame_num += 1
        
        if atoms.calc is not None: energy = float(atoms.get_potential_energy())
        else: energy = 0

        simulation_time, temperature = dyn.get_time(), dyn.temp*eV_to_K

        temp_pdb = StringIO()
        ase.io.write(temp_pdb, atoms, format='proteindatabank')
        atom_string = temp_pdb.getvalue()
        temp_pdb.close()
        data_dict.update({
            "energy": f"{energy} [eV]",
            "simulation_time": f"{simulation_time} [ps]",
            "temperature": f"{temperature} [K]"
        })
        self.upload_queue.put((atom_string, self.frame_num, self.run_id, data_dict))

    def num_files(self):
        """Returns the number of files in the current project."""
        if not self.logged_in:
            print("Not logged in. Cannot list project files.")
            return 0

        if dev: url = "https://alexander-mathiasen--logmd-list-project-dev.modal.run"  # Replace with the actual URL
        else: url = "https://alexander-mathiasen--logmd-list-project.modal.run"  # Replace with the actual URL
        data = {
            "user_id": self.token['email'],
            "token": self.token['token'],
            "project": self.project
        }

        try:
            response = httpx.post(url, json=data)
            if response.status_code == 200:
                result = response.json()
                if "projects" in result:
                    return len(result["projects"]) 
                else:
                    print("Error:", result.get("error", "Unknown error"))
            else:
                print(f"Failed to list project files with status {response.status_code}: {response.text}")
        except Exception as e:
            print("Error while listing project files:", str(e))

        return 0


# Adjectives/Nouns 
adjectives = ["abandoned","able","absolute","adorable","adventurous","academic","acceptable","acclaimed","accomplished","accurate","aching","acidic","acrobatic","active","actual","adept","admirable","admired","adolescent","adorable","adored","advanced","afraid","affectionate","aged","aggravating","aggressive","agile","agitated","agonizing","agreeable","ajar","alarmed","alarming","alert","alienated","alive","all","altruistic","amazing","ambitious","ample","amused","amusing","anchored","ancient","angelic","angry","anguished","animated","annual","another","antique","anxious","any","apprehensive","appropriate","apt","arctic","arid","aromatic","artistic","ashamed","assured","astonishing","athletic","attached","attentive","attractive","austere","authentic","authorized","automatic","avaricious","average","aware","awesome","awful","awkward","babyish","bad","back","baggy","bare","barren","basic","beautiful","belated","beloved","beneficial","better","best","bewitched","big","big-hearted","biodegradable","bite-sized","bitter","black","black-and-white","bland","blank","blaring","bleak","blind","blissful","blond","blue","blushing","bogus","boiling","bold","bony","boring","bossy","both","bouncy","bountiful","bowed","brave","breakable","brief","bright","brilliant","brisk","broken","bronze","brown","bruised","bubbly","bulky","bumpy","buoyant","burdensome","burly","bustling","busy","buttery","buzzing","calculating","calm","candid","canine","capital","carefree","careful","careless","caring","cautious","cavernous","celebrated","charming","cheap","cheerful","cheery","chief","chilly","chubby","circular","classic","clean","clear","clear-cut","clever","close","closed","cloudy","clueless","clumsy","cluttered","coarse","cold","colorful","colorless","colossal","comfortable","common","compassionate","competent","complete","complex","complicated","composed","concerned","concrete","confused","conscious","considerate","constant","content","conventional","cooked","cool","cooperative","coordinated","corny","corrupt","costly","courageous","courteous","crafty","crazy","creamy","creative","creepy","criminal","crisp","critical","crooked","crowded","cruel","crushing","cuddly","cultivated","cultured","cumbersome","curly","curvy","cute","cylindrical","damaged","damp","dangerous","dapper","daring","darling","dark","dazzling","dead","deadly","deafening","dear","dearest","decent","decimal","decisive","deep","defenseless","defensive","defiant","deficient","definite","definitive","delayed","delectable","delicious","delightful","delirious","demanding","dense","dental","dependable","dependent","descriptive","deserted","detailed","determined","devoted","different","difficult","digital","diligent","dim","dimpled","dimwitted","direct","disastrous","discrete","disfigured","disgusting","disloyal","dismal","distant","downright","dreary","dirty","disguised","dishonest","dismal","distant","distinct","distorted","dizzy","dopey","doting","double","downright","drab","drafty","dramatic","dreary","droopy","dry","dual","dull","dutiful","each","eager","earnest","early","easy","easy-going","ecstatic","edible","educated","elaborate","elastic","elated","elderly","electric","elegant","elementary","elliptical","embarrassed","embellished","eminent","emotional","empty","enchanted","enchanting","energetic","enlightened","enormous","enraged","entire","envious","equal","equatorial","essential","esteemed","ethical","euphoric","even","evergreen","everlasting","every","evil","exalted","excellent","exemplary","exhausted","excitable","excited","exciting","exotic","expensive","experienced","expert","extraneous","extroverted","extra-large","extra-small","fabulous","failing","faint","fair","faithful","fake","false","familiar","famous","fancy","fantastic","far","faraway","far-flung","far-off","fast","fat","fatal","fatherly","favorable","favorite","fearful","fearless","feisty","feline","female","feminine","few","fickle","filthy","fine","finished","firm","first","firsthand","fitting","fixed","flaky","flamboyant","flashy","flat","flawed","flawless","flickering","flimsy","flippant","flowery","fluffy","fluid","flustered","focused","fond","foolhardy","foolish","forceful","forked","formal","forsaken","forthright","fortunate","fragrant","frail","frank","frayed","free","French","fresh","frequent","friendly","frightened","frightening","frigid","frilly","frizzy","frivolous","front","frosty","frozen","frugal","fruitful","full","fumbling","functional","funny","fussy","fuzzy","gargantuan","gaseous","general","generous","gentle","genuine","giant","giddy","gigantic","gifted","giving","glamorous","glaring","glass","gleaming","gleeful","glistening","glittering","gloomy","glorious","glossy","glum","golden","good","good-natured","gorgeous","graceful","gracious","grand","grandiose","granular","grateful","grave","gray","great","greedy","green","gregarious","grim","grimy","gripping","grizzled","gross","grotesque","grouchy","grounded","growing","growling","grown","grubby","gruesome","grumpy","guilty","gullible","gummy","hairy","half","handmade","handsome","handy","happy","happy-go-lucky","hard","hard-to-find","harmful","harmless","harmonious","harsh","hasty","hateful","haunting","healthy","heartfelt","hearty","heavenly","heavy","hefty","helpful","helpless","hidden","hideous","high","high-level","hilarious","hoarse","hollow","homely","honest","honorable","honored","hopeful","horrible","hospitable","hot","huge","humble","humiliating","humming","humongous","hungry","hurtful","husky","icky","icy","ideal","idealistic","identical","idle","idiotic","idolized","ignorant","ill","illegal","ill-fated","ill-informed","illiterate","illustrious","imaginary","imaginative","immaculate","immaterial","immediate","immense","impassioned","impeccable","impartial","imperfect","imperturbable","impish","impolite","important","impossible","impractical","impressionable","impressive","improbable","impure","inborn","incomparable","incompatible","incomplete","inconsequential","incredible","indelible","inexperienced","indolent","infamous","infantile","infatuated","inferior","infinite","informal","innocent","insecure","insidious","insignificant","insistent","instructive","insubstantial","intelligent","intent","intentional","interesting","internal","international","intrepid","ironclad","irresponsible","irritating","itchy","jaded","jagged","jam-packed","jaunty","jealous","jittery","joint","jolly","jovial","joyful","joyous","jubilant","judicious","juicy","jumbo","junior","jumpy","juvenile","kaleidoscopic","keen","key","kind","kindhearted","kindly","klutzy","knobby","knotty","knowledgeable","knowing","known","kooky","kosher","lame","lanky","large","last","lasting","late","lavish","lawful","lazy","leading","lean","leafy","left","legal","legitimate","light","lighthearted","likable","likely","limited","limp","limping","linear","lined","liquid","little","live","lively","livid","loathsome","lone","lonely","long","long-term","loose","lopsided","lost","loud","lovable","lovely","loving","low","loyal","lucky","lumbering","luminous","lumpy","lustrous","luxurious","mad","made-up","magnificent","majestic","major","male","mammoth","married","marvelous","masculine","massive","mature","meager","mealy","mean","measly","meaty","medical","mediocre","medium","meek","mellow","melodic","memorable","menacing","merry","messy","metallic","mild","milky","mindless","miniature","minor","minty","miserable","miserly","misguided","misty","mixed","modern","modest","moist","monstrous","monthly","monumental","moral","mortified","motherly","motionless","mountainous","muddy","muffled","multicolored","mundane","murky","mushy","musty","muted","mysterious","naive","narrow","nasty","natural","naughty","nautical","near","neat","necessary","needy","negative","neglected","negligible","neighboring","nervous","new","next","nice","nifty","nimble","nippy","nocturnal","noisy","nonstop","normal","notable","noted","noteworthy","novel","noxious","numb","nutritious","nutty","obedient","obese","oblong","oily","oblong","obvious","occasional","odd","oddball","offbeat","offensive","official","old","old-fashioned","only","open","optimal","optimistic","opulent","orange","orderly","organic","ornate","ornery","ordinary","original","other","our","outlying","outgoing","outlandish","outrageous","outstanding","oval","overcooked","overdue","overjoyed","overlooked","palatable","pale","paltry","parallel","parched","partial","passionate","past","pastel","peaceful","peppery","perfect","perfumed","periodic","perky","personal","pertinent","pesky","pessimistic","petty","phony","physical","piercing","pink","pitiful","plain","plaintive","plastic","playful","pleasant","pleased","pleasing","plump","plush","polished","polite","political","pointed","pointless","poised","poor","popular","portly","posh","positive","possible","potable","powerful","powerless","practical","precious","present","prestigious","pretty","precious","previous","pricey","prickly","primary","prime","pristine","private","prize","probable","productive","profitable","profuse","proper","proud","prudent","punctual","pungent","puny","pure","purple","pushy","putrid","puzzled","puzzling","quaint","qualified","quarrelsome","quarterly","queasy","querulous","questionable","quick","quick-witted","quiet","quintessential","quirky","quixotic","quizzical","radiant","ragged","rapid","rare","rash","raw","recent","reckless","rectangular","ready","real","realistic","reasonable","red","reflecting","regal","regular","reliable","relieved","remarkable","remorseful","remote","repentant","required","respectful","responsible","repulsive","revolving","rewarding","rich","rigid","right","ringed","ripe","roasted","robust","rosy","rotating","rotten","rough","round","rowdy","royal","rubbery","rundown","ruddy","rude","runny","rural","rusty","sad","safe","salty","same","sandy","sane","sarcastic","sardonic","satisfied","scaly","scarce","scared","scary","scented","scholarly","scientific","scornful","scratchy","scrawny","second","secondary","second-hand","secret","self-assured","self-reliant","selfish","sentimental","separate","serene","serious","serpentine","several","severe","shabby","shadowy","shady","shallow","shameful","shameless","sharp","shimmering","shiny","shocked","shocking","shoddy","short","short-term","showy","shrill","shy","sick","silent","silky","silly","silver","similar","simple","simplistic","sinful","single","sizzling","skeletal","skinny","sleepy","slight","slim","slimy","slippery","slow","slushy","small","smart","smoggy","smooth","smug","snappy","snarling","sneaky","sniveling","snoopy","sociable","soft","soggy","solid","somber","some","spherical","sophisticated","sore","sorrowful","soulful","soupy","sour","Spanish","sparkling","sparse","specific","spectacular","speedy","spicy","spiffy","spirited","spiteful","splendid","spotless","spotted","spry","square","squeaky","squiggly","stable","staid","stained","stale","standard","starchy","stark","starry","steep","sticky","stiff","stimulating","stingy","stormy","straight","strange","steel","strict","strident","striking","striped","strong","studious","stunning","stupendous","stupid","sturdy","stylish","subdued","submissive","substantial","subtle","suburban","sudden","sugary","sunny","super","superb","superficial","superior","supportive","sure-footed","surprised","suspicious","svelte","sweaty","sweet","sweltering","swift","sympathetic","tall","talkative","tame","tan","tangible","tart","tasty","tattered","taut","tedious","teeming","tempting","tender","tense","tepid","terrible","terrific","testy","thankful","that","these","thick","thin","third","thirsty","this","thorough","thorny","those","thoughtful","threadbare","thrifty","thunderous","tidy","tight","timely","tinted","tiny","tired","torn","total","tough","traumatic","treasured","tremendous","tragic","trained","tremendous","triangular","tricky","trifling","trim","trivial","troubled","true","trusting","trustworthy","trusty","truthful","tubby","turbulent","twin","ugly","ultimate","unacceptable","unaware","uncomfortable","uncommon","unconscious","understated","unequaled","uneven","unfinished","unfit","unfolded","unfortunate","unhappy","unhealthy","uniform","unimportant","unique","united","unkempt","unknown","unlawful","unlined","unlucky","unnatural","unpleasant","unrealistic","unripe","unruly","unselfish","unsightly","unsteady","unsung","untidy","untimely","untried","untrue","unused","unusual","unwelcome","unwieldy","unwilling","unwitting","unwritten","upbeat","upright","upset","urban","usable","used","useful","useless","utilized","utter","vacant","vague","vain","valid","valuable","vapid","variable","vast","velvety","venerated","vengeful","verifiable","vibrant","vicious","victorious","vigilant","vigorous","villainous","violet","violent","virtual","virtuous","visible","vital","vivacious","vivid","voluminous","wan","warlike","warm","warmhearted","warped","wary","wasteful","watchful","waterlogged","watery","wavy","wealthy","weak","weary","webbed","wee","weekly","weepy","weighty","weird","welcome","well-documented","well-groomed","well-informed","well-lit","well-made","well-off","well-to-do","well-worn","wet","which","whimsical","whirlwind","whispered","white","whole","whopping","wicked","wide","wide-eyed","wiggly","wild","willing","wilted","winding","windy","winged","wiry","wise","witty","wobbly","woeful","wonderful","wooden","woozy","wordy","worldly","worn","worried","worrisome","worse","worst","worthless","worthwhile","worthy","wrathful","wretched","writhing","wrong","wry","yawning","yearly","yellow","yellowish","young","youthful","yummy","zany","zealous","zesty","zigzag"]
nouns = ["people","history","way","art","world","information","map","two","family","government","health","system","computer","meat","year","thanks","music","person","reading","method","data","food","understanding","theory","law","bird","literature","problem","software","control","knowledge","power","ability","economics","love","internet","television","science","library","nature","fact","product","idea","temperature","investment","area","society","activity","story","industry","media","thing","oven","community","definition","safety","quality","development","language","management","player","variety","video","week","security","country","exam","movie","organization","equipment","physics","analysis","policy","series","thought","basis","boyfriend","direction","strategy","technology","army","camera","freedom","paper","environment","child","instance","month","truth","marketing","university","writing","article","department","difference","goal","news","audience","fishing","growth","income","marriage","user","combination","failure","meaning","medicine","philosophy","teacher","communication","night","chemistry","disease","disk","energy","nation","road","role","soup","advertising","location","success","addition","apartment","education","math","moment","painting","politics","attention","decision","event","property","shopping","student","wood","competition","distribution","entertainment","office","population","president","unit","category","cigarette","context","introduction","opportunity","performance","driver","flight","length","magazine","newspaper","relationship","teaching","cell","dealer","finding","lake","member","message","phone","scene","appearance","association","concept","customer","death","discussion","housing","inflation","insurance","mood","woman","advice","blood","effort","expression","importance","opinion","payment","reality","responsibility","situation","skill","statement","wealth","application","city","county","depth","estate","foundation","grandmother","heart","perspective","photo","recipe","studio","topic","collection","depression","imagination","passion","percentage","resource","setting","ad","agency","college","connection","criticism","debt","description","memory","patience","secretary","solution","administration","aspect","attitude","director","personality","psychology","recommendation","response","selection","storage","version","alcohol","argument","complaint","contract","emphasis","highway","loss","membership","possession","preparation","steak","union","agreement","cancer","currency","employment","engineering","entry","interaction","mixture","preference","region","republic","tradition","virus","actor","classroom","delivery","device","difficulty","drama","election","engine","football","guidance","hotel","owner","priority","protection","suggestion","tension","variation","anxiety","atmosphere","awareness","bath","bread","candidate","climate","comparison","confusion","construction","elevator","emotion","employee","employer","guest","height","leadership","mall","manager","operation","recording","sample","transportation","charity","cousin","disaster","editor","efficiency","excitement","extent","feedback","guitar","homework","leader","mom","outcome","permission","presentation","promotion","reflection","refrigerator","resolution","revenue","session","singer","tennis","basket","bonus","cabinet","childhood","church","clothes","coffee","dinner","drawing","hair","hearing","initiative","judgment","lab","measurement","mode","mud","orange","poetry","police","possibility","procedure","queen","ratio","relation","restaurant","satisfaction","sector","signature","significance","song","tooth","town","vehicle","volume","wife","accident","airport","appointment","arrival","assumption","baseball","chapter","committee","conversation","database","enthusiasm","error","explanation","farmer","gate","girl","hall","historian","hospital","injury","instruction","maintenance","manufacturer","meal","perception","pie","poem","presence","proposal","reception","replacement","revolution","river","son","speech","tea","village","warning","winner","worker","writer","assistance","breath","buyer","chest","chocolate","conclusion","contribution","cookie","courage","dad","desk","drawer","establishment","examination","garbage","grocery","honey","impression","improvement","independence","insect","inspection","inspector","king","ladder","menu","penalty","piano","potato","profession","professor","quantity","reaction","requirement","salad","sister","supermarket","tongue","weakness","wedding","affair","ambition","analyst","apple","assignment","assistant","bathroom","bedroom","beer","birthday","celebration","championship","cheek","client","consequence","departure","diamond","dirt","ear","fortune","friendship","funeral","gene","girlfriend","hat","indication","intention","lady","midnight","negotiation","obligation","passenger","pizza","platform","poet","pollution","recognition","reputation","shirt","sir","speaker","stranger","surgery","sympathy","tale","throat","trainer","uncle","youth","time","work","film","water","money","example","while","business","study","game","life","form","air","day","place","number","part","field","fish","back","process","heat","hand","experience","job","book","end","point","type","home","economy","value","body","market","guide","interest","state","radio","course","company","price","size","card","list","mind","trade","line","care","group","risk","word","fat","force","key","light","training","name","school","top","amount","level","order","practice","research","sense","service","piece","web","boss","sport","fun","house","page","term","test","answer","sound","focus","matter","kind","soil","board","oil","picture","access","garden","range","rate","reason","future","site","demand","exercise","image","case","cause","coast","action","age","bad","boat","record","result","section","building","mouse","cash","class","nothing","period","plan","store","tax","side","subject","space","rule","stock","weather","chance","figure","man","model","source","beginning","earth","program","chicken","design","feature","head","material","purpose","question","rock","salt","act","birth","car","dog","object","scale","sun","note","profit","rent","speed","style","war","bank","craft","half","inside","outside","standard","bus","exchange","eye","fire","position","pressure","stress","advantage","benefit","box","frame","issue","step","cycle","face","item","metal","paint","review","room","screen","structure","view","account","ball","discipline","medium","share","balance","bit","black","bottom","choice","gift","impact","machine","shape","tool","wind","address","average","career","culture","morning","pot","sign","table","task","condition","contact","credit","egg","hope","ice","network","north","square","attempt","date","effect","link","post","star","voice","capital","challenge","friend","self","shot","brush","couple","debate","exit","front","function","lack","living","plant","plastic","spot","summer","taste","theme","track","wing","brain","button","click","desire","foot","gas","influence","notice","rain","wall","base","damage","distance","feeling","pair","savings","staff","sugar","target","text","animal","author","budget","discount","file","ground","lesson","minute","officer","phase","reference","register","sky","stage","stick","title","trouble","bowl","bridge","campaign","character","club","edge","evidence","fan","letter","lock","maximum","novel","option","pack","park","plenty","quarter","skin","sort","weight","baby","background","carry","dish","factor","fruit","glass","joint","master","muscle","red","strength","traffic","trip","vegetable","appeal","chart","gear","ideal","kitchen","land","log","mother","net","party","principle","relative","sale","season","signal","spirit","street","tree","wave","belt","bench","commission","copy","drop","minimum","path","progress","project","sea","south","status","stuff","ticket","tour","angle","blue","breakfast","confidence","daughter","degree","doctor","dot","dream","duty","essay","father","fee","finance","hour","juice","limit","luck","milk","mouth","peace","pipe","seat","stable","storm","substance","team","trick","afternoon","bat","beach","blank","catch","chain","consideration","cream","crew","detail","gold","interview","kid","mark","match","mission","pain","pleasure","score","screw","sex","shop","shower","suit","tone","window","agent","band","block","bone","calendar","cap","coat","contest","corner","court","cup","district","door","east","finger","garage","guarantee","hole","hook","implement","layer","lecture","lie","manner","meeting","nose","parking","partner","profile","respect","rice","routine","schedule","swimming","telephone","tip","winter","airline","bag","battle","bed","bill","bother","cake","code","curve","designer","dimension","dress","ease","emergency","evening","extension","farm","fight","gap","grade","holiday","horror","horse","host","husband","loan","mistake","mountain","nail","noise","occasion","package","patient","pause","phrase","proof","race","relief","sand","sentence","shoulder","smoke","stomach","string","tourist","towel","vacation","west","wheel","wine","arm","aside","associate","bet","blow","border","branch","breast","brother","buddy","bunch","chip","coach","cross","document","draft","dust","expert","floor","god","golf","habit","iron","judge","knife","landscape","league","mail","mess","native","opening","parent","pattern","pin","pool","pound","request","salary","shame","shelter","shoe","silver","tackle","tank","trust","assist","bake","bar","bell","bike","blame","boy","brick","chair","closet","clue","collar","comment","conference","devil","diet","fear","fuel","glove","jacket","lunch","monitor","mortgage","nurse","pace","panic","peak","plane","reward","row","sandwich","shock","spite","spray","surprise","till","transition","weekend","welcome","yard","alarm","bend","bicycle","bite","blind","bottle","cable","candle","clerk","cloud","concert","counter","flower","grandfather","harm","knee","lawyer","leather","load","mirror","neck","pension","plate","purple","ruin","ship","skirt","slice","snow","specialist","stroke","switch","trash","tune","zone","anger","award","bid","bitter","boot","bug","camp","candy","carpet","cat","champion","channel","clock","comfort","cow","crack","engineer","entrance","fault","grass","guy","hell","highlight","incident","island","joke","jury","leg","lip","mate","motor","nerve","passage","pen","pride","priest","prize","promise","resident","resort","ring","roof","rope","sail","scheme","script","sock","station","toe","tower","truck","witness","a","you","it","can","will","if","one","many","most","other","use","make","good","look","help","go","great","being","few","might","still","public","read","keep","start","give","human","local","general","she","specific","long","play","feel","high","tonight","put","common","set","change","simple","past","big","possible","particular","today","major","personal","current","national","cut","natural","physical","show","try","check","second","call","move","pay","let","increase","single","individual","turn","ask","buy","guard","hold","main","offer","potential","professional","international","travel","cook","alternative","following","special","working","whole","dance","excuse","cold","commercial","low","purchase","deal","primary","worth","fall","necessary","positive","produce","search","present","spend","talk","creative","tell","cost","drive","green","support","glad","remove","return","run","complex","due","effective","middle","regular","reserve","independent","leave","original","reach","rest","serve","watch","beautiful","charge","active","break","negative","safe","stay","visit","visual","affect","cover","report","rise","walk","white","beyond","junior","pick","unique","anything","classic","final","lift","mix","private","stop","teach","western","concern","familiar","fly","official","broad","comfortable","gain","maybe","rich","save","stand","young","fail","heavy","hello","lead","listen","valuable","worry","handle","leading","meet","release","sell","finish","normal","press","ride","secret","spread","spring","tough","wait","brown","deep","display","flow","hit","objective","shoot","touch","cancel","chemical","cry","dump","extreme","push","conflict","eat","fill","formal","jump","kick","opposite","pass","pitch","remote","total","treat","vast","abuse","beat","burn","deposit","print","raise","sleep","somewhere","advance","anywhere","consist","dark","double","draw","equal","fix","hire","internal","join","kill","sensitive","tap","win","attack","claim","constant","drag","drink","guess","minor","pull","raw","soft","solid","wear","weird","wonder","annual","count","dead","doubt","feed","forever","impress","nobody","repeat","round","sing","slide","strip","whereas","wish","combine","command","dig","divide","equivalent","hang","hunt","initial","march","mention","smell","spiritual","survey","tie","adult","brief","crazy","escape","gather","hate","prior","repair","rough","sad","scratch","sick","strike","employ","external","hurt","illegal","laugh","lay","mobile","nasty","ordinary","respond","royal","senior","split","strain","struggle","swim","train","upper","wash","yellow","convert","crash","dependent","fold","funny","grab","hide","miss","permit","quote","recover","resolve","roll","sink","slip","spare","suspect","sweet","swing","twist","upstairs","usual","abroad","brave","calm","concentrate","estimate","grand","male","mine","prompt","quiet","refuse","regret","reveal","rush","shake","shift","shine","steal","suck","surround","anybody","bear","brilliant","dare","dear","delay","drunk","female","hurry","inevitable","invite","kiss","neat","pop","punch","quit","reply","representative","resist","rip","rub","silly","smile","spell","stretch","stupid","tear","temporary","tomorrow","wake","wrap","yesterday"]

