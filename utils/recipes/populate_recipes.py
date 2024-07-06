# cspell:ignoreFile


import os
import random
import django
from django.utils.text import slugify
from django.conf import settings
from recipes.models import Recipe, Category, User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def populate_recipes():
    categories = Category.objects.all()
    authors = User.objects.all()

    if not categories:
        Category.objects.create(name="Default Category")
        categories = Category.objects.all()

    if not authors:
        User.objects.create_user(username="defaultuser", password="password")
        authors = User.objects.all()

    titles = ["Spaghetti Carbonara", "Chicken Alfredo", "Beef Stroganoff",
              "Vegetable Stir Fry", "Shrimp Scampi", "Lemon Chicken",
              "Fish Tacos", "Pasta Primavera", "Chicken Curry", "Beef Tacos"]

    descriptions = ["A classic Italian pasta dish.",
                    "Creamy and delicious chicken pasta.",
                    "Rich and hearty beef dish.",
                    "Quick and easy vegetable stir fry.",
                    "Garlic butter shrimp pasta.",
                    "Tangy and flavorful lemon chicken.",
                    "Fresh and tasty fish tacos.",
                    "Colorful and healthy pasta dish.",
                    "Spicy and creamy chicken curry.",
                    "Savory and filling beef tacos."]

    preparation_steps_list = ["<p>Pellentesque habitant morbi tristique "
                              "senectus et netus et malesuada fames ac turpis"
                              "egestas. Vestibulum tortor quam, feugiat vitae,"
                              "ultricies eget, tempor sit amet, ante. Donec eu"
                              "libero sit amet quam egestas semper. Aenean "
                              "ultricies mi vitae est. Mauris placerat elefend"
                              "leo. Quisque sit amet est et sapien ullamcorper"
                              "pharetra. Vestibulum erat wisi, condimentum sed"
                              "commodo vitae, ornare sit amet, wisi. Aenean "
                              "fermentum, elit eget tincidunt condimentum, ero"
                              "ipsum rutrum orci, sagittis tempus lacus enim"
                              "ui. Donec non enim in turpis pulvinar facilisis"
                              "Ut felis. Praesent dapibus, neque id cursus "
                              "faucibus, tortor neque egestas augue, eu "
                              "vulputate magna eros eu erat. Aliquam erat "
                              "volutpat. Nam dui mi, tincidunt quis, accumsan "
                              "porttitor, facilisis luctus, metus</p>",
                              "<h1>HTML Ipsum Presents</h1><p><strong>"
                              "Pellentesque habitant morbi tristique</strong> "
                              "senectus et netus et malesuada fames ac turpis "
                              "egestas. Vestibulum tortor quam, feugiat vitae,"
                              "ultricies eget, tempor sit amet, ante. Donec eu"
                              "libero sit amet quam egestas semper. <em>Aenean"
                              "ultricies mi vitae est.</em> Mauris placerat "
                              "eleifend leo. Quisque sit amet est et sapien "
                              "ullamcorper pharetra. Vestibulum erat wisi, "
                              "condimentum sed, <code>commodo vitae</code>, "
                              "ornare sit amet, wisi. Aenean fermentum, elit "
                              "eget tincidunt condimentum, eros ipsum rutrum "
                              "orci, sagittis tempus lacus enim ac dui. "
                              "<a href='#'>Donec non enim</a> in turpis "
                              "pulvinar facilisis. Ut felis.</p><h2>"
                              "Header Level 2</h2><ol><li>Lorem ipsu dolor sit"
                              "amet, consectetuer adipiscing elit.</li><li>"
                              "Aliquam tincidunt mauris eu risus.</li></ol>"
                              "<blockquote><p>Lorem ipsum dolor sit amet, "
                              "consectetur adipiscing elit. Vivamus magna. "
                              "Cras in mi at felis aliquet congue. Ut a est "
                              "eget ligula molestie gravida. Curabitur massa."
                              "Donec eleifend, libero at sagittis mollis, "
                              "tellus est malesuada tellus, at luctus turpis"
                              "elit sit amet quam. Vivamus pretium ornare "
                              "est.</p></blockquote><h3>Header Level 3</h3>"
                              "<ul><li>Lorem ipsum dolor sit amet,"
                              "consectetuer adipiscing elit.</li>"
                              "<li>Aliquam tincidunt mauris eu risus."
                              "</li></ul>",
                              ]

    units = ["minutes", "people"]

    images = [
        'recipes/covers/2024/07/06/image1.jpg',
        'recipes/covers/2024/07/06/image2.jpg',
        'recipes/covers/2024/07/06/image3.jpg',
        'recipes/covers/2024/07/06/image4.jpg',
        'recipes/covers/2024/07/06/image5.jpg',
        'recipes/covers/2024/07/06/image6.jpg',
        'recipes/covers/2024/07/06/image7.jpg',
        'recipes/covers/2024/07/06/image8.jpg',
    ]

    for i in range(10):
        title = random.choice(titles)
        description = random.choice(descriptions)
        slug = slugify(title)
        preparation_time = random.randint(10, 60)
        servings = random.randint(1, 8)
        preparation_steps = random.choice(preparation_steps_list)
        preparation_steps_is_html = True
        is_published = True
        cover = random.choice(images)
        preparation_time_unit = units[0]
        servings_unit = units[1]

        # Seleciona aleatoriamente uma categoria e um autor
        category = random.choice(categories)
        author = random.choice(authors)

        Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
            category=category,
            author=author
        )

    print("10 receitas foram criadas com sucesso!")


if __name__ == "__main__":
    populate_recipes()
