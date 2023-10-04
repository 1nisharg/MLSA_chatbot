from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Menu options and their corresponding answers



menu_options = {
    'What is Microsoft Learn Student Ambassadors, KIIT Chapter?': 'Microsoft Learn Student Ambassadors (MLSA) at KIIT Chapter is a community of passionate students who are enthusiastic about technology and want to make a positive impact on their campus and in the broader community.',
    'What are the Upcoming Events of MLSA, KIIT Chapter?': 'We regularly organize tech events, workshops, hackathons, and seminars. Stay tuned to our social media channels for updates on upcoming events.',
    'What are the Past Events of MLSA, KIIT Chapter?': '''The Past Events of Microsoft Learn Student Ambassadors, KIIT Chapter include:

1. Stark Expo : Conducted On 3rd September 2023 with 2000+ Participants

2. Eye S.py Squid : Conducted On 16th April 2023 with 1368 Participants

3. KALKI Computer Vision: Conducted On 11th February 2023 with 844 Participants

4. KALKI AR/VR: Conducted On 11th February 2023 with 844 Participants

5. KALKI Scavenger Hunt: Conducted On 11th February 2023 with 844 Participants

6. Project Wing 3.0: Conducted On 13th November 2022''',
    'What are the Domains of MLSA, KIIT Chapter?': 'Our chapter focuses on domains like artificial intelligence, web development, cloud computing, and more. We have diverse interests among our members.',
    'How to Join MLSA, KIIT Chapter?': 'Joining MLSA, KIIT Chapter is easy! Attend our events, workshops, and meetings to become a member. Follow us on social media for updates on our activities.',
    'How to Contact Us?': 'You can reach out to us via email at contact@mlsakiitchapter.com or through our social media channels. We are always happy to connect with fellow tech enthusiasts!'
}


@app.route('/')
def home():
    return render_template('menu.html', menu_options=menu_options)

@app.route('/<selected_option>')
def menu_option(selected_option):
    # Replace spaces with underscores in the selected option
    selected_option = selected_option.replace('_', ' ')

    if selected_option in menu_options:
        # Render the template corresponding to the selected menu option
        return render_template(f'option{list(menu_options.keys()).index(selected_option) + 1}.html', menu_options=menu_options)
    else:
        # Redirect to the home page if the option is not found
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
