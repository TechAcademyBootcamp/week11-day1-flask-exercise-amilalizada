# Flask Exercise
Melumat:
Blog proyekti yaradın, hansı ki, istifadəçilər öz bloglarını əlavə edə bilir. 
1. Flask Project yaradın. auth və core app-ları və fayl strukturlarınızı qurun. 
2. Dərsdə istifadə etdiyimiz templatedən istifadə edərək (template link: `https://startbootstrap.com/templates/blog-home/`) Blog list səhifəsini qurun. Həmin səhifədə Search funksionallığını quraşdırın. Search edərkən içində bazada title-da search-ə uyğun olan blog-ları səhifəyə əlavə edin.
3. Blog List-de `Read More` click etdikdə həmin səhifənin blog-un ətraflı səhifəsi açılsın. Həmin səhifənin dizayn-i `index.html` -səhifəsində olan bir blog-un görünüşü şəklində olsun. Əlavə olaraq həmin səhifədə `Update Blog` və `Delete Blog` butttonları olsun hansı ki, `Update Blog`-a click edəndə `create` səhifəsinə bənzər `update` səhifəsi açılsın. `Delete Blog`-a click edəndə blog-u bazadan silsin.
controller asagidaki sekilde yazilmalidir:
```
@core.route('/update/<id>')
def update(id)
```
## Qeyd Update Create Delete Etdikde səhifələrlə flask-lar çıxarmaq mütləqdir. 