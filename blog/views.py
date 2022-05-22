from django.shortcuts import render

all_posts = [
    {
        'slug': 'first_post',
        'post_title': 'Hello Django',
        'post_image': 'mountains.jpg',
        'post_author': 'Mohammad Reza',
        'post_updated_time': '19 May 2022',
        'post_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'post_content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris 
    rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi 
    tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et 
    molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. 
    Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut 
    tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet 
    facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas 
    volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas 
    sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. """
    },
    {
        'slug': 'second_post',
        'post_title': 'Lets deep into Django',
        'post_image': 'woods.jpg',
        'post_author': 'Mohammad Reza',
        'post_updated_time': '20 May 2022',
        'post_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'post_content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris 
    rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi 
    tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et 
    molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. 
    Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut 
    tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet 
    facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas 
    volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas 
    sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. """
    },
    {
        'slug': 'third_post',
        'post_title': 'Coding with python',
        'post_image': 'coding.jpg',
        'post_author': 'Mohammad Reza',
        'post_updated_time': '21 May 2022',
        'post_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'post_content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris 
    rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi 
    tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et 
    molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. 
    Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut 
    tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet 
    facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas 
    volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas 
    sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. """
    },
    {
        'slug': 'fourth_post',
        'post_title': 'Final Post',
        'post_image': 'mra.jpg',
        'post_author': 'Mohammad Reza',
        'post_updated_time': '22 May 2022',
        'post_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
        'post_content': """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. Egestas purus viverra accumsan in nisl nisi. Arcu cursus vitae congue mauris 
    rhoncus aenean vel elit scelerisque. In egestas erat imperdiet sed euismod nisi porta lorem mollis. Morbi 
    tristique senectus et netus. Mattis pellentesque id nibh tortor id aliquet lectus proin. Sapien faucibus et 
    molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. 
    Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut 
    tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet 
    facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas 
    volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas 
    sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. """
    },
]


def starting_page(request):
    return render(request, 'blog/index.html', {'last_posts': all_posts[:3]})


def posts(request):
    return render(request, 'blog/posts.html', {'all_posts': all_posts})


def single_post(request, slug):
    chosen_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/single_post.html', {'post': chosen_post})
