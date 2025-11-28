from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'database'

urlpatterns = [
    # ホーム
    path('', views.home, name='home'),

    # ログイン・ログアウト・サインアップ
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='database/password_reset.html', email_template_name='database/password_reset_email.txt', subject_template_name='database/password_reset_subject.txt', success_url='/password_reset/done/',), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='database/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='database/password_reset_confirm.html', success_url='/reset/done/'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='database/password_reset_complete.html'), name='password_reset_complete'),

    # お問い合わせ・登録ページ

    path('register/', views.register_view, name='register'),
    path('contact/', views.contact, name='contact'),
    path('contact/complete/', views.contact_complete_view, name='contact_complete'),

    # ドラクエ1攻略
    path('dq1/guide/', views.dq1_guide, name='dq1_guide'),
    path('dq1/html/', views.dq1_html, name='dq1_html'),

    # ドラクエ1 サブページ
    path('dq1/story/', views.dq1_story_list, name='dq1_story_list'),
    path('dq1/boss/', views.dq1_boss_list, name='dq1_boss_list'),
    path('dq1/items/', views.dq1_items_list, name='dq1_items_list'),
    path('dq1/map/', views.dq1_map_list, name='dq1_map_list'),
    path('dq1/monster/', views.dq1_monster_list, name='dq1_monster_list'),
    path('dq1/scrolls/', views.dq1_scrolls_list, name='dq1_scrolls_list'),
    path('dq1_medal/', views.dq1_medal_list, name='dq1_medal_list'),
    path('dq1/map/<slug:map_slug>/', views.dq1_detail, name='dq1_detail'),
    path('dq1/equip/', views.dq1_equip_list, name='dq1_equip_list'),

    # ドラクエ1 章ごとのページ
    path('dq1/section1/', views.dq1_section1_content, name='dq1_section1_content'),
    path('dq1/section2/', views.dq1_section2_content, name='dq1_section2_content'),
    path('dq1/section3/', views.dq1_section3_content, name='dq1_section3_content'),
    path('dq1/section4/', views.dq1_section4_content, name='dq1_section4_content'),
    path('dq1/section5/', views.dq1_section5_content, name='dq1_section5_content'),
    path('dq1/section6/', views.dq1_section6_content, name='dq1_section6_content'),

    # ドラクエ1 ボスごとのページ
    path('dq1/kandata/', views.dq1_kandata, name='dq1_kandata'),
    path('dq1/youjutsushi/', views.dq1_youjutsushi, name='dq1_youjutsushi'),
    path('dq1/yoroinokishi/', views.dq1_yoroinokishi, name='dq1_yoroinokishi'),
    path('dq1/dragon/', views.dq1_dragon, name='dq1_dragon'),
    path('dq1/darkdreamer/', views.dq1_darkdreamer, name='dq1_darkdreamer'),
    path('dq1/golem/', views.dq1_golem, name='dq1_golem'),
    path('dq1/dragonfly/', views.dq1_dragonfly, name='dq1_dragonfly'),
    path('dq1/dragonzombie/', views.dq1_dragonzombie, name='dq1_dragonzombie'),
    path('dq1/alienfly/', views.dq1_alienfly, name='dq1_alienfly'),
    path('dq1/akumanokishi/', views.dq1_akumanokishi, name='dq1_akumanokishi'),
    path('dq1/murdergoyle/', views.dq1_murdergoyle, name='dq1_murdergoyle'),
    path('dq1/ekusodasu/', views.dq1_ekusodasu, name='dq1_ekusodasu'),
    path('dq1/ryuou/', views.dq1_ryuou, name='dq1_ryuou'),

    # ドラクエ1 マップごとのページ（全 URL 名を維持）
    path('dq1/map/amenohokora/', TemplateView.as_view(template_name="database/dq1_map/amenohokora.html"), name='dq1_amenohokora'),
    path('dq1/map/domudo-ra/', TemplateView.as_view(template_name="database/dq1_map/domudo-ra.html"), name='dq1_domudo-ra'),
    path('dq1/map/dowa-hunodoukutu/', TemplateView.as_view(template_name="database/dq1_map/dowa-hunodoukutu.html"), name='dq1_dowa-hunodoukutu'),
    path('dq1/map/garai/', TemplateView.as_view(template_name="database/dq1_map/garai.html"), name='dq1_garai'),
    path('dq1/map/garainohaka/', TemplateView.as_view(template_name="database/dq1_map/garainohaka.html"), name='dq1_garainohaka'),
    path('dq1/map/himitunohanabatake/', TemplateView.as_view(template_name="database/dq1_map/himitunohanabatake.html"), name='dq1_himitunohanabatake'),
    path('dq1/map/iwanakishima/', TemplateView.as_view(template_name="database/dq1_map/iwanakishima.html"), name='dq1_iwanakishima'),
    path('dq1/map/iwayamanodoukutu/', TemplateView.as_view(template_name="database/dq1_map/iwayamanodoukutu.html"), name='dq1_iwayamanodoukutu'),
    path('dq1/map/kaidounoyadoya/', TemplateView.as_view(template_name="database/dq1_map/kaidounoyadoya.html"), name='dq1_kaidounoyadoya'),
    path('dq1/map/maira/', TemplateView.as_view(template_name="database/dq1_map/maira.html"), name='dq1_maira'),
    path('dq1/map/mayoinomori/', TemplateView.as_view(template_name="database/dq1_map/mayoinomori.html"), name='dq1_mayoinomori'),
    path('dq1/map/medaruounoshiro/', TemplateView.as_view(template_name="database/dq1_map/medaruounoshiro.html"), name='dq1_medaruounoshiro'),
    path('dq1/map/merukido/', TemplateView.as_view(template_name="database/dq1_map/merukido.html"), name='dq1_merukido'),
    path('dq1/map/namonakihaikyo/', TemplateView.as_view(template_name="database/dq1_map/namonakihaikyo.html"), name='dq1_namonakihaikyo'),
    path('dq1/map/numatinodoukutu/', TemplateView.as_view(template_name="database/dq1_map/numatinodoukutu.html"), name='dq1_numatinodoukutu'),
    path('dq1/map/radato-mu/', TemplateView.as_view(template_name="database/dq1_map/radato-mu.html"), name='dq1_radato-mu'),
    path('dq1/map/radato-munishinoshima/', TemplateView.as_view(template_name="database/dq1_map/radato-munishinoshima.html"), name='dq1_radato-munishinoshima'),
    path('dq1/map/rimuruda-ru/', TemplateView.as_view(template_name="database/dq1_map/rimuruda-ru.html"), name='dq1_rimuruda-ru'),
    path('dq1/map/rotonodoukutu/', TemplateView.as_view(template_name="database/dq1_map/rotonodoukutu.html"), name='dq1_rotonodoukutu'),
    path('dq1/map/ryuounoshiro/', TemplateView.as_view(template_name="database/dq1_map/ryuounoshiro.html"), name='dq1_ryuounoshiro'),
    path('dq1/map/seinaruhokora/', TemplateView.as_view(template_name="database/dq1_map/seinaruhokora.html"), name='dq1_seinaruhokora'),
    path('dq1/map/seireinohokora/', TemplateView.as_view(template_name="database/dq1_map/seireinohokora.html"), name='dq1_seireinohokora'),
    path('dq1/map/tabibitonokyoukai/', TemplateView.as_view(template_name="database/dq1_map/tabibitonokyoukai.html"), name='dq1_tabibitonokyoukai'),
    path('dq1/map/tabibitonoyadoya/', TemplateView.as_view(template_name="database/dq1_map/tabibitonoyadoya.html"), name='dq1_tabibitonoyadoya'),
    path('dq1/map/wasureraretahaikyo/', TemplateView.as_view(template_name="database/dq1_map/wasureraretahaikyo.html"), name='dq1_wasureraretahaikyo'),
    path('dq1/map/youseinokakurezato/', TemplateView.as_view(template_name="database/dq1_map/youseinokakurezato.html"), name='dq1_youseinokakurezato'),

    # ドラクエ1 装備・アイテム・モンスター・スクロール
    path('scroll/<str:scroll_name>/', views.scroll_view, name='scroll_detail'),
    path('monster/<str:monster_name>/', views.monster_view, name='monster_detail'),
    path('item/<str:item_name>/', views.item_view, name='item_detail'),
    path('equip/<str:equip_name>/', views.equip_view, name='equip_detail'),

    # ドラクエ2
    path('dq2/', views.dq2_guide, name='dq2_guide'),

    # クラフトピア
    path('craftopia/guide/', views.cp_guide, name='cp_guide'),
    path('craftopia/main/', views.craftopia_guide, name='craftopia_guide'),
    path('guide/story/', views.cp_story_list, name='cp_story_list'),
    path('guide/kihon/', views.cp_kihon_list, name='cp_kihon_list'),
    path('guide/bukisyu/', views.cp_bukisyu_list, name='cp_bukisyu_list'),
    path('guide/boss/', views.cp_boss_list, name='cp_boss_list'),
    path('guide/mahou/', views.cp_mahou_list, name='cp_mahou_list'),
    path('guide/seikatu/', views.cp_seikatu_list, name='cp_seikatu_list'),
    path('guide/sentou/', views.cp_sentou_list, name='cp_sentou_list'),
    path('guide/teima/', views.cp_teima_list, name='cp_teima_list'),
    path('guide/torikku', views.cp_torikku_list, name='cp_torikku_list'),
    path('guide/giza/', views.cp1_story_giza, name='cp1_story_giza'),
    path('guide/miruulin/', views.cp2_story_miruulin, name='cp2_story_miruulin'),
    path('guide/yaden/', views.cp3_story_yaden, name='cp3_story_yaden'),
    path('guide/oowatatu/', views.cp4_story_oowatatu, name='cp4_story_oowatatu'),
    path('guide/burigandain/', views.cp5_story_burigandain, name='cp5_story_burigandain'),
    path('guide/syarubato/', views.cp6_story_syarubato, name='cp6_story_syarubato'),
    path('guide/unneferu/', views.cp7_story_unneferu, name='cp7_story_unneferu'),
    path('guide/maiazuma/', views.cp8_story_maiazuma, name='cp8_story_maiazuma'),
    path('guide/kazan/', views.cp9_story_kazan, name='cp9_story_kazan'),




    # REPO
    path('repo/monsters/', views.monster_list, name='monster_list'),
    path('items/', views.item_list, name='item_list'),
    path('repo/shop/', views.shop_item_list, name='shop_item_list'),
    path('level-guides/', views.level_guide_list, name='level_guide_list'),
    path('repo/', views.guide_repo, name='guide_repo'),

    # 個別ゲームページ
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
    path('toggle_favorite/<str:model_type>/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),

    path('', views.home, name='home'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
