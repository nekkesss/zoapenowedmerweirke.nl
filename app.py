from flask import Flask, render_template

app = Flask(__name__)

# Sample meme data
memes = [
    {
        'title': 'Doppe',
        'image': 'https://img.nieuwsblad.be/9QIjfvHOsc7yGRWSJi8vL14rWMI=/1280x853/smart/https%3A%2F%2Fstatic.nieuwsblad.be%2FAssets%2FImages_Upload%2F2005%2F11%2F16%2FA21_STEMPEL.MM.jpg',
        'description': 'nowed mer weirke al te lang dakweirker gewest'
    }
]

# Sample local cafes data
cafes = [
    {
        'name': 'Bing Chilling',
        'image': 'https://api.opcafegaan.be/image/profileimages/550/500/crop/webp/chill-out1-vorselaar.jpg',
        'description': 'Da is hie genen boekewinkel godverdoeme.'
    },
    {
        'name': 'Araaaaaaaaaab',
        'image': 'https://static.gva.be/Assets/Images_Upload/2018/08/23/c1733b2a-9fe5-11e8-93a7-4e412f8d40e5_web_scale_0.050505_0.050505__.jpg',
        'description': 'De gunther beton is van beton.'
    },
    {
        'name': 'heirbeirg',
        'image': 'https://static.gva.be/Assets/Images_Upload/2022/09/21/57548973-bd68-4276-a8de-adb479283e4b.jpg',
        'description': 'spauwcello is aanwezig'
    },
    {
        'name': 'den tip',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlaIqX54E64d_Qsf4HGQerzmcB8NkvfVa5AA&s',
        'description': 'den tip is den tip'
    },
    {
        'name': 'tspieke',
        'image': 'https://be.top10place.com/img_files/320865564621680',
        'description': 'pro darters'
    },
    {
        'name': 'de dreevoes',
        'image': 'https://vorselaar.be/wp-content/uploads/2021/11/sportcafe3.jpg',
        'description': 'teraske doen?'
    },
    {
        'name': 'toekomst',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1bZuURSoIaMKLYzhruRrcOFH7XGB9AqFW0A&s',
        'description': 'den toekomst van zuipedoppenowedmerweirk.nl'
    },
    {
        'name': 'zomerbar gabberdoenk',
        'image': 'https://images0.persgroep.net/rcs/zrbep8j9HiJTrrMWq_mFs3mOQUg/diocontent/203544437/_fitwidth/694/?appId=21791a8992982cd8da851550a453bd7f&quality=0.8',
        'description': 'bucht bareke'
    },
    {
        'name': 'zomerbar vusseleir',
        'image': 'https://fastly.4sqi.net/img/general/600x600/69095366_4lJD1ssDUbDelJ3V7eroDaxBprPaewqwSDhRRMFc-8g.jpg',
        'description': 'komaan dj hetenteen'
    }
]

@app.route('/')
def home():
    return render_template('index.html', memes=memes, cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
