import re
import wordcloud as wc
import matplotlib.pyplot as plt

files = [
    'how_is_my_discipline_interdisciplinary',
    'my_discipline_made_visual',
    'unlearning_to_learn',
    'midpoint_reflection'
]

def clean_text(text):
    ''' Returns the given string in all lowercase without punctuation. '''
    cleaned_text = []
    for word in text.lower().split():
        word = re.sub("[^\w\s]", "", word)
        cleaned_text.append(word)
    return ' '.join(cleaned_text)

def generate_wordclouds(data):
    '''
    Takes a list of dictionaries storing discussion board posts and produce
    a wordcloud for each post.
    '''
    plt.figure(figsize=(10, 6))
    index = 1
    for post in data:
        cloud = wc.WordCloud().generate(post['clean'])
        plt.subplot(2, 2, index)
        plt.title(post['title'])
        plt.imshow(cloud)
        plt.axis('off')
        index += 1
    plt.show()

def main():
    data = []
    for file_name in files:
        with open('{}.md'.format(file_name)) as file:
            title = file.readline().strip()
            post = file.read()
            data.append({
                'title': title[4:],
                'post': post,
                'clean': clean_text(post)
            })
    
    generate_wordclouds(data)

if __name__ == '__main__':
    main()

