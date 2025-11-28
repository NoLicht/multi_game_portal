from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from .models import Game
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Character, Item, Dungeon
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.template import TemplateDoesNotExist
from .models import Monster, RepoItem, LevelGuide,ShopItem, MapInfo, LevelEffect, OrbDamage
from django.views.decorators.http import require_POST
from .models import Comment
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    page_id = 'home'

    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get("comment")
        if content:
            Comment.objects.create(
                user=request.user,
                page_id=page_id,
                content=content
            )
        return redirect('database:home')

    comments = Comment.objects.filter(page_id=page_id).order_by('created_at')

    return render(request, 'database/home.html', {
        "comments": comments,
        "page_id": page_id
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('database:home')
    else:
        form = SignUpForm()
    return render(request, 'database/signup.html', {'form': form})

def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 認証処理
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('database:home')
        else:
            error = "ユーザー名またはパスワードが違います"

    return render(request, 'database/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('database:home')

def dq1_view(request):
    return render(request, 'database/dq1.html')

def dq1_guide(request):
    sections = range(1, 7)
    return render(request, 'database/dq1_content/dq1.html', {'sections': sections})

def dq2_guide(request):
    return render(request, 'database/dq2.html')

def cp_guide(request):
    return render(request, 'database/craftopia.html')

def cp_bukisyu_list(request):
    return render(request, 'database/cp_content/cp_bukisyu_list.html')

def cp_boss_list(request):
    return render(request, 'database/cp_content/cp_boss_list.html')

def cp_mahou_list(request):
    return render(request, 'database/cp_content/cp_mahou_list.html')

def cp_seikatu_list(request):
    return render(request, 'database/cp_content/cp_seikatu_list.html')

def cp_sentou_list(request):
    return render(request, 'database/cp_content/cp_sentou_list.html')

def cp_teima_list(request):
    return render(request, 'database/cp_content/cp_teima_list.html')

def cp_torikku_list(request):
    return render(request, 'database/cp_content/cp_torikku_list.html')

def cp1_story_giza(request):
    return render(request, 'database/cp_content\cp1_story_giza.html')

def cp2_story_miruulin(request):
    return render(request, 'database/cp_content/cp2_story_miruulin.html')

def cp3_story_yaden(request):
    return render(request, 'database/cp_content/cp3_story_yaden.html')

def cp4_story_oowatatu(request):
    return render(request, 'database/cp_content/cp4_story_oowatatu.html')

def cp5_story_burigandain(request):
    return render(request, 'database/cp_content/cp5_story_burigandain.html')

def cp6_story_syarubato(request):
    return render(request, 'database/cp_content/cp6_story_syarubato.html')

def cp7_story_unneferu(request):
    return render(request, 'database/cp_content/cp7_story_unneferu.html')

def cp8_story_maiazuma(request):
    return render(request, 'database/cp_content/cp8_story_maiazuma.html')

def cp9_story_kazan(request):
    return render(request, 'database/cp_content/cp9_story_kazan.html')

def cp_story_list(request):
    return render(request, 'database/cp_content/cp_story_list.html')

def cp_kihon_list(request):
    return render(request, 'database/cp_content/cp_kihon_list.html')

def craftopia_guide(request):
    return render(request, 'database/cp_content/cp_tutorial_list.html')

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'database/game_detail.html', {'game': game})

@login_required
def toggle_favorite(request, model_type, pk):
    model_map = {
        'character': Character,
        'item': Item,
        'dungeon': Dungeon,
    }
    if model_type not in model_map:
        return JsonResponse({'error': 'invalid type'}, status=400)

    obj = get_object_or_404(model_map[model_type], pk=pk)
    if request.user in obj.favorited_by.all():
        obj.favorited_by.remove(request.user)
        favorited = False
    else:
        obj.favorited_by.add(request.user)
        favorited = True

    return JsonResponse({'favorited': favorited})

def contact_view(request):
    return render(request, 'database/contact.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('database:home')
    else:
        form = UserCreationForm()
    return render(request, 'database/register.html', {'form': form})

def dq1_html(request):
    return render(request, 'database/dq1_content/dq1.html')

def dq1_section1_content(request):
    return render(request, 'database/sections/dq1_section1_content.html')

def dq1_section2_content(request):
    return render(request, 'database/sections/dq1_section2_content.html')

def dq1_section3_content(request):
    return render(request, 'database/sections/dq1_section3_content.html')

def dq1_section4_content(request):
    return render(request, 'database/sections/dq1_section4_content.html')

def dq1_section5_content(request):
    return render(request, 'database/sections/dq1_section5_content.html')

def dq1_section6_content(request):
    return render(request, 'database/sections/dq1_section6_content.html')

def dq1_kandata(request):
    return render(request, 'database/dq1_boss_detail/dq1_kandata.html')

def dq1_youjutsushi(request):
    return render(request, 'database/dq1_boss_detail/dq1_youjutsushi.html')

def dq1_yoroinokishi(request):
    return render(request, 'database/dq1_boss_detail/dq1_yoroinokishi.html')

def dq1_dragon(request):
    return render(request, 'database/dq1_boss_detail/dq1_dragon.html')

def dq1_darkdreamer(request):
    return render(request, 'database/dq1_boss_detail/dq1_darkdreamer.html')

def dq1_golem(request):
    return render(request, 'database/dq1_boss_detail/dq1_golem.html')

def dq1_dragonfly(request):
    return render(request, 'database/dq1_boss_detail/dq1_dragonfly.html')

def dq1_dragonzombie(request):
    return render(request, 'database/dq1_boss_detail/dq1_dragonzombie.html')

def dq1_alienfly(request):
    return render(request, 'database/dq1_boss_detail/dq1_alienfly.html')

def dq1_akumanokishi(request):
    return render(request, 'database/dq1_boss_detail/dq1_akumanokishi.html')

def dq1_murdergoyle(request):
    return render(request, 'database/dq1_boss_detail/dq1_murdergoyle.html')

def dq1_ekusodasu(request):
    return render(request, 'database/dq1_boss_detail/dq1_ekusodasu.html')

def dq1_ryuou(request):
    return render(request, 'database/dq1_boss_detail/dq1_ryuou.html')

def dq1_story_list(request):
    return render(request, 'database/dq1_content/dq1_story_list.html')

def dq1_boss_list(request):
    return render(request, 'database/dq1_content/dq1_boss_list.html')

def dq1_items_list(request):
    return render(request, 'database/dq1_content/dq1_items_list.html')

def dq1_map_list(request):
    return render(request, 'database/dq1_content/dq1_map_list.html')

def dq1_scrolls_list(request):
    return render(request, 'database/dq1_content/dq1_scrolls_list.html')

def dq1_medal_list(request):
    return render(request, 'database/dq1_content/dq1_medal_list.html')

def dq1_monster_list(request):
    return render(request, 'database/dq1_content/dq1_monster_list.html')

def dq1_equip_list(request):
    return render(request, 'database/dq1_content/dq1_equip_list.html')

def dq1_boss_list(request):
    # ボス情報のリスト
    bosses = [
        {
            "name": "カンダタ",
            "image": "database/images/dq1/boss/kandata.jpg",
            "level": 10,
            "points": [
                "こぶんを再優先で倒す",
                "ヒャダルコでこぶんを一掃する",
                "カンダタには火炎斬りが有効"
            ],
            "location": "チャート1 「岩山の洞窟」"
        },
        {
            "name": "ようじゅつし",
            "image": "database/images/dq1/boss/youjutsushi.jpg",
            "level": 11,
            "points": [
                "デインが有効",
                "マホトーンで呪文を封じる"
            ],
            "location": "チャート1 「岩山の洞窟」"
        },
        {
            "name": "よろいのきし",
            "image": "database/images/dq1/boss/yoroinokishi.jpg",
            "level": 21,
            "points": [
                "うけながしが有効",
                "デイン系で弱点をつく",
                "よろいのきしから倒す"
            ],
            "location": "チャート2 「妖精の隠れ里」"
        },
        {
            "name": "ドラゴン",
            "image": "database/images/dq1/boss/dragon.jpg",
            "level": 21,
            "points": [
                "ドラゴン斬りが有効",
                "火炎軽減の防具を装備",
                "ようせいの剣で守備力を上げる",
                "ビーストモード中は大ぼうぎょ"
            ],
            "location": "チャート2 「沼地の洞窟」"
        },
        {
            "name": "よろいのきし",
            "image": "database/images/dq1/boss/yoroinokishi.jpg",
            "level": 21,
            "points": [
                "うけながしが有効",
                "デイン系で弱点をつく",
                "よろいのきしから倒す"
            ],
            "location": "チャート2 「妖精の隠れ里」"
        },
        {
            "name": "ダークドリーマー",
            "image": "database/images/dq1/boss/darkdreamer.jpg",
            "level": 23,
            "points": [
                "てんばつの杖が有効",
                "マジックバリアで呪文を軽減"
            ],
            "location": "チャート3 「迷いの森」"
        },
        {
            "name": "ゴーレム",
            "image": "database/images/dq1/boss/golem.jpg",
            "level": 27,
            "points": [
                "ようせいのふえで眠らせる",
                "ようせいの剣で守備力を上げる",
                "しんくう斬りが有効"
            ],
            "location": "チャート3 「メルキド」"
        },
        {
            "name": "ドラゴンフライ",
            "image": "database/images/dq1/boss/dragonfly.jpg",
            "level": 30,
            "points": [
                "ドラゴン斬りで1体ずつ処理する",
                "火炎軽減の防具を装備"
            ],
            "location": "チャート3 「岩泣き島」"
        },
        {
            "name": "ドラゴンゾンビ",
            "image": "database/images/dq1/boss/dragonzombie.jpg",
            "level": 32,
            "points": [
                "目覚ましリングを装備",
                "吹雪軽減の防具を装備",
                "フバーハでブレスを軽減",
                "ベギラゴンが有効"
            ],
            "location": "チャート4 「妖精の隠れ里」"
        },
        {
            "name": "エイリアンフライ",
            "image": "database/images/dq1/boss/alienfly.jpg",
            "level": 32,
            "points": [
                "行動パターンを把握する",
                "ブレス軽減防具を装備",
                "2連ブレスは大ぼうぎょ",
                "取り巻きは全体攻撃で処理",
                "ドラゴン斬りが有効"
            ],
            "location": "チャート4 「マイラ」"
        },
        {
            "name": "あくまのきし",
            "image": "database/images/dq1/boss/akumanokishi.jpg",
            "level": 33,
            "points": [
                "やいばのよろいを装備する",
                "めざましリングを装備する",
                "ようせいの剣で守備力を上げる",
                "超ちからため→あくま斬りが有効"
            ],
            "location": "チャート4 「ドムドーラ」"
        },
        {
            "name": "マーダーゴイル",
            "image": "database/images/dq1/boss/murdergoyle.jpg",
            "level": 34,
            "points": [
                "やいばのよろいを装備する",
                "ようせいの剣で守備力を上げる",
                "うけながしが有効",
                "回復アイテムを買っておく"
            ],
            "location": "チャート4 「雨のほこら」"
        },
        {
            "name": "エクソダス",
            "image": "database/images/dq1/boss/ekusodasu.jpg",
            "level": 35,
            "points": [
                "やいばのよろいを装備する",
                "ようせいの剣で守備力を上げる",
                "回復アイテムを買っておく"
            ],
            "location": "チャート4 「精霊のほこら」"
        },
        {
            "name": "りゅうおう",
            "image": "database/images/dq1/boss/ryuou1.jpg",
            "level": 40,
            "points": [
                "炎攻撃を無効化する",
                "ささやきのみつを持っておく",
                "めざましリングを装備する",
                "ようせいの剣で守備力を上げる"
            ],
            "location": "チャート5 「竜王の城」"
        },
        {
            "name": "竜王",
            "image": "database/images/dq1/boss/ryuou2.jpg",
            "level": 40,
            "points": [
                "炎攻撃を無効化する",
                "竜王のバフ行動後は大ぼうぎょ",
                "みかわしきゃくで物理攻撃を避ける"
            ],
            "location": "チャート5 「竜王の城」"
        },
        
    ]

    return render(request, "database/dq1_content/dq1_boss_list.html", {"bosses": bosses})

MAP_DATA = {
    'rotonodoukutu': {
        'name': 'ロトの洞窟',
    },
    'amenohokora': {
        'name': '雨のほこら',
    },
    'iwayamanodoukutu': {
        'name': '岩山の洞窟',
    },
    'numatinodoukutu': {
        'name': '沼地の洞窟',
    },
    'dowa-hunodoukutu': {
        'name': 'ドワーフの洞窟',
    },
    'mayoinomori': {
        'name': '迷いの森',
    },
    'iwanakishima': {
        'name': '岩泣き島',
    },
    'domudo-ra': {
        'name': 'ドムドーラ',
    },
    'garainohaka': {
        'name': 'ガライの墓',
    },
    'ryuounoshiro': {
        'name': '竜王の城',
    },
    'radato-mu': {
        'name': 'ラダトーム',
    },
    'maira': {
        'name': 'マイラ',
    },
    'garai': {
        'name': 'ガライ',
    },
    'youseinokakurezato': {
        'name': '妖精の隠れ里',
    },
    'rimuruda-ru': {
        'name': 'リムルダール',
    },
    'medaruounoshiro': {
        'name': 'メダル王の城',
    },
    'merukido': {
        'name': 'メルキド',
    },
    'tabibitonokyoukai': {
        'name': '旅人の教会',
    },
    'wasureraretahaikyo': {
        'name': '忘れられた廃墟',
    },
    'kaidounoyadoya': {
        'name': '街道の宿屋',
    },
    'namonakihaikyo': {
        'name': '名もなき廃墟',
    },
    'himitunohanabatake': {
        'name': 'ひみつの花畑',
    },
    'tabibitonoyadoya': {
        'name': '旅人の宿屋',
    },
    'seireinohokora': {
        'name': '精霊のほこら',
    },
    'seinaruhokora': {
        'name': '聖なるほこら',
    },
    'radato-munishinoshima': {
        'name': 'ラダトーム西の島',
    },
}

def dq1_detail(request, map_slug):
    template_name = f'database/dq1_map/{map_slug}.html'
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404("ページが見つかりません")
    
SCROLL_TEMPLATES = [
    'akumagiri', 'baria', 'behoimu', 'bi-suto', 'hyadain', 'hyadaruko', 'hyado', 'kutibue', 'mahosute', 'mahyadogiri', 'meisou', 'mirakuru', 'remira-ma', 'rihoimi', 'seishin', 'shinobiashi', 'sunakemuri', 'tikaratame', 'toramana', 'touzoku', 'yaibakudaki', 'zonbigiri'
]

def scroll_view(request, scroll_name):
    if scroll_name not in SCROLL_TEMPLATES:
        raise Http404("スクロールが存在しません")
    template_path = f'database/dq1_scrolls/{scroll_name}.html'
    return render(request, template_path)

MONSTER_TEMPLATES =[
    'suraimu', 'suraimubesu', 'doraki-', 'zinmentyou', 'mahoutuaki', 'go-suto', 'yamanezumi', 'baburusuraimu', 'me-da', 'poizunto-do', 'gizumo', 'yuurei', 'hoimisuraimu', 'obakekinoko', 'animaruzonbi', 'waraibukuro', 'riza-dohurai', 'oosasori', 'ribingudeddo', 'dokuimomushi', 'guntaigani', 'meizidoraki-', 'ayashiikage', 'obakearikui', 'hitokuiga', 'madoushi', 'gaikotu', 'dororu', 'metorogo-suto', 'matango', 'doraki-ma', 'koumoriotoko', 'oonezumi', 'hitokuibako', 'bariidodoggu', 'bebi-satan', 'rikanto', 'shiryou', 'samayouyoroi', 'doruido', 'shiryounokishi', 'medo-sabo-ru', 'kimera', 'rikantomamuru', 'tetunosasori', 'antobea', 'hanta-hurai', 'hi-togizumo', 'kusattashitai', 'yoroinokishi', 'kagenokishi', 'shinigami', 'madohando', 'dororumeizi', 'me-daro-do', 'kaenmukade', 'shinosasori', 'odoruhouseki', 'desujakkaru', 'suraimutumuri', 'meizikimera', 'maddookkusu', 'syado-', 'metarusuraimu', 'genjutushi', 'go-gonheddo', 'zinmenju', 'shibireageha', 'behomasuraimu', 'zigokunoyoroi', 'andeddoman', 'go-rudoman', 'go-dodon', 'kimendoushi', 'doragonhurai', 'ganirasu', 'shibirekurage', 'minide-mon', 'akumanomedama', 'daimadou', 'ga-goiru', 'mimikku', 'gaikotukenshi', 'herugo-suto', 'gu-ru', 'shirueto', 'doragonzonbi', 'maounokage', 'sukarugon', 'hurosutogizumo', 'suto-nman', 'suta-kimera', 'buraddohando', 'tororu', 'ki-sudoragon', 'sukarunaito', 'udora-', 'kira-rikanto', 'tororukingu', 'so-doido', 'haguremetaru', 'da-kuai', 'shinigaminokishi', 'da-sudoragon'
]

def monster_view(request, monster_name):
    if monster_name not in MONSTER_TEMPLATES:
        raise Http404("スクロールが存在しません")
    template_path = f'database/dq1_monster/{monster_name}.html'
    return render(request, template_path)

ITEM_TEMPLATES = [
    'yakusou', 'jouyakusou', 'tokuyakusou', 'mahounoseisui', 'kenjanoseisui', 'eruhunonomigusuri', 'inorinoyubiwa', 'dokukeshisou', 'manu-hasou', 'sasayakinomitu', 'seisui', 'madarakumoito', 'dokuganokona', 'baikirumin', 'kimeranotubasa', 'inotinoishi', 'tikaranotane', 'mamorinotane', 'sutaminanotane', 'kashikosanotane', 'subayasanotane', 'rakkunotane', 'inotinokinomi', 'hushiginakinomi', 'youseinohue', 'ginnotategoto', 'nioibukuro', 'tatakainodoramu', 'mirakurunomakimono', 'yaibakudakinomakimono', 'zonbigirinomakimono', 'akumagirinomakimono', 'mahyadogirinomakimono', 'meisounomakimono', 'seishinnomakimono', 'tikaratamenomakimono', 'bi-sutonomakimono', 'sunakemurinomakimono', 'touzokunomakimono', 'shinobiashinomakimono', 'kutibuenomakimono', 'toramananomakimono', 'remira-manomakimono', 'hyadonomakimono', 'hyadarukonomakimono', 'hyadainnomakimono', 'behoimunomakimono', 'rihoiminomakimono', 'barianomakimono', 'mahosutenomakimono', 'sekainotizu', 'touzokunokagi', 'mahounokagi', 'saigonokagi', 'hikarinotama', 'taiyounoishi', 'nizinoshizuku', 'taiyounomonshou', 'hoshinomonshou', 'tukinomonshou', 'mizunomonshou', 'inotinomonshou', 'oujonokubikazari', 'kagayakisou', 'mezamenohana', 'tomoshibinoshiroppu', 'hikarutane', 'humetunohonoo', 'gekkounoshizuku', 'hoshikuzunosuna', 'wakimizunokesshou', 'kireinamizu', 'kumonosu', 'nazonokona', 'abunaiekisu', 'yakekogetahane', 'matatabisou', 'sasayakinojueki', 'iyashinohutaba'
]

def item_view(request, item_name):
    if item_name not in ITEM_TEMPLATES:
        raise Http404("スクロールが存在しません")
    template_path = f'database/dq1_item/{item_name}.html'
    return render(request, template_path)

EQUIP_TEMPLATES = [
    'dounoturugi', 'haganenoturugi', 'youseinoturugi', 'kusanaginoturugi', 'yuuwakunoturugi', 'honoonoturugi', 'hubukinoturugi', 'rotonoturugi', 'morohanoturugi', 'hakainoturugi', 'seinarunaihu', 'konbou', 'tetunoono', 'mazinnoono', 'takezao', 'tetunoyari', 'doragonkira-', 'sabakinotue', 'amagumonotue', 'tenbatunotue', 'eiyuunotue', 'togenomuti', 'haganenomuti', 'basuta-wippu', 'akumanomuti', 'guringamunomuti', 'bu-meran', 'yaibanobu-meran', 'tuinsuwaro-', 'honoonobu-meran', 'metaruwingu', 'kawanotate', 'urokonotate', 'raitoshi-rudo', 'koorinotate', 'mahounotate', 'huuzinnotate', 'honoonotate', 'mikagaminotate', 'mira-shi-rudo', 'rotonotate', 'seidounotate', 'doragonshi-rudo', 'o-gahshi-rudo', 'hametunotate', 'onabenohuta', 'tetukabuto', 'tekkamen', 'mougyuuherumu', 'tiryokunokabuto', 'rotonokabuto', 'hannyanomen', 'hukounokabuto', 'kawanoboushi', 'kinoboushi', 'kazenoboushi', 'hushiginaboushi', 'yamabikonoboushi', 'ta-ban', 'kagenota-ban', 'kegawanohu-do', 'fantomumasuku', 'kawanoyoroi', 'tetunoyoroi', 'haganenoyoroi', 'mahounoyoroi', 'zonbimeiru', 'doragonmeiru', 'gaianoyoroi', 'yaibanoyoroi', 'bandeddomeiru', 'honoonoyoroi', 'rotonoyoroi', 'zigokunoyoroi', 'nunonohuku', 'kawanohuku', 'tabibitonohuku', 'kusarikatabira', 'mikawashinohuku', 'hadenahuku', 'shinobinohuku', 'hushiginaborero', 'yaminokoromo', 'narikinbesuto', 'kegawanobesuto', 'hayatenobesuto', 'taijunomanto', 'sutetekopantu', 'nekogurumi', 'inugurumi', 'hayatenoringu', 'mezamashiringu', 'mangetunoringu', 'riseinoringu', 'nigenigeringu', 'tikaranoyubiwa', 'rubi-noudewa', 'ishinokatura', 'interimegane', 'suraimupiasu', 'honoonoiyaringu', 'koorinoiyaringu', 'kaizokuounokubikazari', 'shinokubikazari', 'noroinoberuto', 'usaginoshippo', 'shiawasenokutu', 'ryuunouroko', 'mayokenosuzu', 'rotonoshirushi'
]

def equip_view(request, equip_name):
    if equip_name not in EQUIP_TEMPLATES:
        raise Http404("スクロールが存在しません")
    template_path = f'database/dq1_equip/{equip_name}.html'
    return render(request, template_path)

# REPO
def monster_list(request):
    monsters = Monster.objects.all()
    return render(request, 'database/repo/monster_list.html', {
        'monsters': monsters
    })

def item_list(request):
    melee_items = RepoItem.objects.filter(category='melee')
    ranged_items = RepoItem.objects.filter(category='ranged')
    throw_items = RepoItem.objects.filter(category='throw')
    trap_items = RepoItem.objects.filter(category='trap')
    treasure_items = RepoItem.objects.filter(category='treasure')

    return render(request, 'database/repo/item_list.html', {
        'melee_items': melee_items,
        'ranged_items': ranged_items,
        'throw_items': throw_items,
        'trap_items': trap_items,
        'treasure_items': treasure_items,
    })

def shop_item_list(request):
    upgrade_items = ShopItem.objects.filter(category='upgrade', available=True)
    heal_items = ShopItem.objects.filter(category='heal', available=True)
    drone_items = ShopItem.objects.filter(category='drone', available=True)
    other_items = ShopItem.objects.filter(category='other', available=True)
    return render(request, 'database/repo/shop_item_list.html', {
        'upgrade_items': upgrade_items,
        'heal_items': heal_items,
        'drone_items': drone_items,
        'other_items': other_items,
    })


def level_guide_list(request):
    guides = LevelGuide.objects.order_by('level')
    return render(request, 'database/repo/level_guide_list.html', {
        'guides': guides
    })

def guide_repo(request):
    return render(request, 'database/repo/guide_repo.html')

def monster_list(request):
    monsters = Monster.objects.prefetch_related("attacks").all()
    return render(request, "database/repo/monster_list.html", {"monsters": monsters})

def level_guide_list(request):
    stages = LevelGuide.objects.all()
    return render(request, 'database/repo/level_guide_list.html', {'stages': stages})

def level_guide_list(request):
    stages = LevelGuide.objects.all()
    level_effects = LevelEffect.objects.all()
    orb_damages = OrbDamage.objects.all()
    return render(
        request,
        'database/repo/level_guide_list.html',
        {
            'stages': stages,
            'level_effects': level_effects,
            'orb_damages': orb_damages,
        }
    )

@require_POST
def logout_view(request):
    logout(request)
    return redirect('database:home')

TEMPLATE_MAPPING = {
    "section1": "dq1_section1_content",
    "section2": "dq1_section2_content",
    "section3": "dq1_section3_content",
    "section4": "dq1_section4_content",
    "section5": "dq1_section5_content",
    "section6": "dq1_section6_content",
}

def content_view(request, template_name):
    if template_name not in TEMPLATE_MAPPING:
        raise Http404("ページが見つかりません")

    page_id = TEMPLATE_MAPPING[template_name]

    # 投稿処理
    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get("comment")
        if content:
            Comment.objects.create(
                user=request.user,
                page_id=page_id,
                content=content
            )
        return redirect(request.path)

    # コメント取得
    comments = Comment.objects.filter(page_id=page_id).order_by('created_at')

    # レンダリング
    return render(request, f"database/sections/{page_id}.html", {
        "comments": comments,
        "page_id": page_id
    })

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'database:home'))

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            subject = f"[問い合わせ] {name}"
            body = f"送信者: {name}\nメール: {email}\n\n内容:\n{message}"
            recipient_list = ['admin@example.com']

            send_mail(subject, body, email, recipient_list)
            messages.success(request, "問い合わせが送信されました。")
            return redirect('database:contact_complete')
        else:
            messages.error(request, "全ての項目を入力してください。")

    return render(request, 'database/contact.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            subject = f"[問い合わせ] {name}"
            body = f"送信者: {name}\nメール: {email}\n\n内容:\n{message}"
            recipient_list = ['shougonosuke@gmail.com']

            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
            )

            return redirect('database:contact_complete')
        else:
            messages.error(request, "全ての項目を入力してください。")

    return render(request, 'database/contact.html')


def contact_complete_view(request):
    """
    問い合わせ送信完了ページ
    """
    return render(request, 'database/contact_complete.html')
