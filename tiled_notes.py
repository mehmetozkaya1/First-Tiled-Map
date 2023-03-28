import pygame, sys
from pytmx.util_pygame import load_pygame # İhtiyacımız olan modül içerisinden istediğimiz metodu import ediyoruz.

class Tile(pygame.sprite.Sprite): # Bir Tile class'ı oluşturuyoruz. Sprite'lardan kalıtım alacak.
    def __init__(self,pos,surf,groups): # Hepsi için bir pozisyon, surface ve groups değeri veriyoruz.
        super().__init__(groups) # Sprite class'ını init ediyoruz.
        self.image = surf # Fotoğrafını ayarlıyoruz.
        self.rect = self.image.get_rect(topleft = pos) # Ve bir rect oluşturuyoruz.

pygame.init() # Pygame'i init ediyoruz. (başlatıyoruz.)
screen = pygame.display.set_mode((1280,720)) # Oyunun ekran boyutunu ayarlıyoruz.
tmx_data = load_pygame('data/tmx/basic.tmx') # Oyun tmx dosyamızın konumunu vererek yüklüyoruz.
sprite_group = pygame.sprite.Group() # Bir sprite grubu oluşturduk.
# Sprite grubuna eleman ekleyip ekranımızda çizdirebiliriz.

# Tüm layer'ları dönmek gezmek:
for layer in tmx_data.visible_layers: # Tüm görünür layerlar arasından
    # if layer.name in ('Floor','Plants and rocks','Pipes'): # Eğer layer adımız bu üçünden biri ise
    if hasattr(layer,'data'): # Tile layer'lar data attr'ına sahipken objeler değil.
        for x,y,surf in layer.tiles(): # Bu layer'ların her bir x,y ve surface'ları için
            pos = (x * 128, y * 128) # Tile boyutumuz ile çarpıyoruz ki konumu elde edelim.
            Tile(pos=pos,surf=surf, groups= sprite_group) # Ve bir Tile nesnesi oluşturuyor ve değişkenlerini veriyoruz.
            # pos ile her bir tile pozisyonuna verdiğimiz özgü surface'ları veriyoruz.
            # grup olarak ise de sprite_group'umuzu veriyoruz.

# Objelerin çizimi:
for obj in tmx_data.objects: # Tüm objeleri geziyoruz.
    pos = (obj.x, obj.y) # Her bir objenin konumu
    """ 1-
    if obj.image: # Eğer bir image'ı varsa objenin (Marker ve Shape'lerin yok.)
        surf = obj.image # Her bir objeye surface'ını veriyoruz.
    Tile(pos= pos, surf= surf, groups= sprite_group)
    """
    # 2-
    if obj.type in ('Building','Vegetation'): # Eğer objenin türü bir building ya da vegetation ise.
        surf = obj.image 
        Tile(pos= pos, surf= surf, groups= sprite_group)
    

"""
# print(tmx_data) # Bir TiledMap objesi olduğunu görüyoruz.
# print(dir(tmx_data)) # tmx_data üzerinden kullanabileceğimiz birçok özellik var.

# Layer'lara ulaşmak:
# print(tmx_data.layers) # Bu şekilde bu dosya içerisindeki tüm layer'ları görebiliriz.
# print(tmx_data.visible_layers) # Görünür olan tüm layer'ları tek bir generator obje içerisinde toplar.
# for layer in tmx_data.visible_layers: # Her bir visible_layer içerisinden
#     print(layer) # Tüm layer'ları tek tek yazdır.
# # !! Eğer Tiled içerisinde bir layer'ı görünmez yapar ve kaydederseniz visible layers içerisinde bulamazsınız.
# # Görünmeyen layer olarak harita sınırları (borderları) kullanabilirsiniz.

# print(tmx_data.layernames) # Tüm layer'ların isimlerini getirir.

# print(tmx_data.get_layer_by_name('Floor')) # Layer ismiyle istenilen layer'ı çağırabiliriz.

# for obj in tmx_data.objectgroups: # Tüm obje layerları içerisinden
#     print(obj) # Tüm obje layerlarını yazdır.

# Tile'ları getirmek
layer = tmx_data.get_layer_by_name('Floor') # Floor layer'ımı layer değişkenine attım.
# print(dir(layer)) # layer değişkeni üzerinden kullanabileceğimiz komutlara bakıyoruz.
print(layer.tiles()) # Bu şekilde bir generator obje oluşturduk.

for tile in layer.tiles(): # Tüm tile'lar için
    print(tile) # Her bir tile'ı yaz.
# Bu şekilde her bir Tile'ın konumunu x ve y şeklinde veren (haritadaki satır ve sütünda bulunan Tile sayısına göre)
# ve içerisinde bir Surface bulunan tüm Tile'ları yazdırdık.

for x,y,surf in layer.tiles(): # Tüm bilgiler için bu döngü yeterlidir.
    print(x * 128)
    print(y * 128)
    print(surf)
# Tüm Tile'ların x,y pozisyonları ve surface'larını yazdırdık.
# Bu x ve y pozisyonları size sadece hangi satır ve sütun olduğunu verir. Oyununuz içerisinde bu değerleri her bir tile boyutu ile çarparak kullanmalısınız.
# Bizim haritamızda her bir tile 128*128 büyüklüğünde bu yüzden 128 ile çarpmalıyız.

print(layer.data) # data komutu ile bir csv dosyası olarak kullanabilirsiniz.

print(layer.name) # Layer ismini yazdırır.
print(layer.id) # Layer id'sini yazdırır.

# Objeleri getirme:
object_layer = tmx_data.get_layer_by_name('Objects') # Objects ismindeki layer'ı çağırıyorum. Bu layer aynı zamanda bir object layer'ı.
print(dir(object_layer)) # Bu obje ile kullanabileceğimiz komutları görebiliriz.

for obj in object_layer: # Obje layer'ı içerisinden
    print(obj) # Tüm objeleri yazdır. Bu komut ile isimlerini tek tek alabiliriz.

for obj in tmx_data.objects: # Yukarıdakinin aynısını bu şekilde de alabiliriz.
    print(obj)

print(dir(obj)) # Her bir obje için kullanabileceğimiz komuları görebiliriz.

for obj in object_layer:
    print(obj.x) # Her bir objenin x koordinatı. Bu x direkt koordinat bilgisi
    print(obj.y) # Her bir objenin y koordinatı. Bu y direkt koordinat bilgisi
    print(obj.image) # Her bir objenin surface'ı

for obj in object_layer: # Her bir obje layer'ı içerisinden
    if obj.type == 'Shape': # Obje türü Shape olan tüm objelerin verilen attr ver.
        if obj.name == 'Marker': # Ve eğer obje ismi de marker ise
            print(obj) # Tüm objeleri yazdır.
            print(obj.x)
            print(obj.y)
        if obj.name == 'Rectangle':
            print(obj)
            print(obj.x)
            print(obj.y)
            print(obj.width) # Genişliği
            print(obj.height) # Uznunluğu
            print(obj.points) # Rect'in her bir köşesinin koordinatlarını döndürür.
        if obj.name == 'Ellipse':
            print(obj)
        if obj.name == 'Polygon':
            print(obj.as_points) # as_point rect'in konumlarını getirir.
            print(obj.points) # Bu da poligonun konumlarını getirir.

# Bu marker pozisyonlarını oyuncunuzun spawnlanması için kullanabilirsizniz.
"""

while True: # Oyunun çalışacağı sonsuz döngü
    for event in pygame.event.get(): # pygame içerisindeki tüm event'ler için
        if event.type == pygame.QUIT: # Eğer çıkma komutunu verdiysek.
            pygame.quit() # Pygame'i durdur.
            sys.exit() # Dosyalardan tamamen çıkış yap.
    
    screen.fill('black') # Ekranı siyaha boya
    sprite_group.draw(screen) # Sprite grubunu ekranıma çizdiriyorum.
    
    for obj in tmx_data.objects: # Tüm objeleri geziyoruz.
        pos = (obj.x, obj.y) # Her bir objenin konumu
        if obj.type == 'Shape':
            if obj.name == 'Marker': # Ve eğer obje ismi de marker ise
                pygame.draw.circle(screen,'red',(obj.x,obj.y),5) # Her bir marker için r=5 olan bir çember çizdik.
            if obj.name == 'Rectangle':
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height) # Gerçek bir rect'e çevirdik. (l,t,w,h)
                pygame.draw.rect(screen,'yellow',rect) # Rect'i ekrana çizdiriyoruz.
            if obj.name == 'Ellipse':
                rect = pygame.Rect(obj.x,obj.y,obj.width,obj.height) # Bir rect oluşturdum.
                pygame.draw.ellipse(screen,'blue',rect) # Ekrana çizdik.
            if obj.name == 'Polygon':
                points = [(point.x,point.y) for point in obj.points]
                pygame.draw.polygon(screen,'green',points) # Ekrana çizdirdik.

    pygame.display.update() # Ekran görüntüsünü sürekli olarak yenile.