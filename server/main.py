from flask import Flask, jsonify, send_from_directory, request, send_file
from flask_cors import CORS
from pytube import YouTube, Playlist
import os
import json
import socket
import wikipedia

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'



@app.route('/get_response', methods=['GET', 'POST'])
def get_response():
    user_message = request.form['user_message']

    try:
        result = wikipedia.summary(user_message) 
    except Exception as e:
        result = "Not found..."

    
    return jsonify({'bot_reply': result})


# login form

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get JSON data from the request
    email = data.get('username')
    password = data.get('password')

    # Process the form data (you can add your logic here)
    if(email+".json" in os.listdir(f"../profile")):
        
        with open(f'../profile/{email}.json', 'r') as file:
            json_data = json.load(file)

        if(password == json_data['password']):
            return jsonify({'message': '/'})
        
        else:
           return jsonify({'message': 'Password not match...'}) 
        
    else:
        return jsonify({'message': 'Email not match...'})

# registor page
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json  # Get JSON data from the request
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    repassword = data.get('repassword')

    # Process the form data (you can add your logic here)
    # print(username,password,email,repassword)

    json_string = f'{{"username": "{username}", "email": "{email}", "password": "{password}"}}'
    json_data = json.loads(json_string)

    with open(f"../profile/{email}.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    return jsonify({'message': '/login.html'})

# videos database
@app.route('/videos')
def videos():
    playlist_link = "https://youtube.com/playlist?list=PLZoTAELRMXVNxYFq_9MuiUdn2YnlFqmMK&si=dTxlBZX3blEkJj1k"
    video_links = Playlist(playlist_link).video_urls

    video_titles = []
    for link in video_links:
        video_titles.append([YouTube(link).title,YouTube(link).thumbnail_url])


    return (video_titles)

# Notes database
@app.route('/notes')
def notes():
    # folder_path = 'D:\\mysite\\College_site\\perfect-learn\\server\\notes'
    folder_path = os.getcwd()+"/notes"

    # Get the list of file names in the folder
    notes_data = []
    folder_names = os.listdir(folder_path)
    for folder in folder_names:
        folder_data = []
        folder_data.append([folder])
        file_data = []
        for file in os.listdir(folder_path+"/"+folder):
            file_data.append([file.replace(" ","_"),file.replace(" ","_").replace(".pdf",".png")])
        folder_data.append(file_data)
        notes_data.append(folder_data)

    return notes_data


# Downloading database
@app.route('/d/<topic>/<foldername>/<filename>', methods=['GET'])
def download_file(topic,foldername,filename):
    # Path to the file you want to download
    file_path = os.getcwd()+"/"+ topic +"/" + foldername +"/"+filename
    print(file_path)
    return send_file(file_path, as_attachment=True)



# image database
@app.route('/images/<filename>')
def get_image(filename):
    # Serve images from the 'uploads' folder
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/upload_notes', methods=['POST'])
def upload_notes():
    title = request.form['title']
    description = request.form['description']
    pdf_file = request.files['file']

    if not os.path.exists(app.config['UPLOAD_FOLDER']+"/notes"):
        os.makedirs(app.config['UPLOAD_FOLDER']+"/notes")

    # Save the PDF file to the 'uploads' folder
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER']+"/notes", pdf_file.filename)
    pdf_file.save(pdf_path)

    # Process the title, description, and pdf_file as needed
    # For example, save the PDF file to a server folder

    # Return a JSON response
    response = {'status': 'success', 'message': 'File uploaded successfully!'}
    return jsonify(response)

@app.route('/upload_pyqs', methods=['POST'])
def upload_pyqs():
    title = request.form['title']
    description = request.form['description']
    pdf_file = request.files['file']

    if not os.path.exists(app.config['UPLOAD_FOLDER']+"/pyqs"):
        os.makedirs(app.config['UPLOAD_FOLDER']+"/pyqs")

    # Save the PDF file to the 'uploads' folder
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER']+"/pyqs", pdf_file.filename)
    pdf_file.save(pdf_path)

    # Process the title, description, and pdf_file as needed
    # For example, save the PDF file to a server folder

    # Return a JSON response
    response = {'status': 'success', 'message': 'File uploaded successfully!'}
    return jsonify(response)

@app.route('/upload_videos', methods=['POST'])
def upload_videos():
    title = request.form['title']
    description = request.form['description']
    pdf_file = request.files['file']

    if not os.path.exists(app.config['UPLOAD_FOLDER']+"/videos"):
        os.makedirs(app.config['UPLOAD_FOLDER']+"/videos")

    # Save the PDF file to the 'uploads' folder
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER']+"/videos", pdf_file.filename)
    pdf_file.save(pdf_path)

    # Process the title, description, and pdf_file as needed
    # For example, save the PDF file to a server folder

    # Return a JSON response
    response = {'status': 'success', 'message': 'File uploaded successfully!'}
    return jsonify(response)


@app.route('/save_changes', methods=['POST'])
def save_changes():
    full_name = request.form.get('full_name')
    email = request.form.get('email')

    mobile = request.form.get('mobile')
    address = request.form.get('address')
    website = request.form.get('website')
    github = request.form.get('github')
    twitter = request.form.get('twitter')
    instagram = request.form.get('instagram')
    facebook = request.form.get('facebook')

    
    with open(f'../profile/{email}.json', 'r') as file:
        json_data = json.load(file)

    # Process the data as needed (e.g., save to database)
    json_string = f'{{"username": "{full_name}", "email": "{email}", "password": "{json_data["password"]}",  "mobile": "{mobile}",  "address": "{address}",  "website": "{website}",  "github": "{github}",  "twitter": "{twitter}",  "instagram": "{instagram}",  "facebook": "{facebook}"}}'

    # print(json_string)
    json_data = json.loads(json_string)

    with open(f"../profile/{email}.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    # Return a JSON response
    response = {'status': 'success', 'message': 'Changes saved successfully!'}
    return jsonify(response)

@app.route('/getinfo', methods=['POST'])
def getinfo():
    email = request.json.get('username')
    # email = request.form.get('email')
    password = request.json.get('password')

        # Process the form data (you can add your logic here)
    if(email+".json" in os.listdir(f"../profile")):

        with open(f'../profile/{email}.json', 'r') as file:
            json_data = json.load(file)
        return json_data
     
    else:
        return jsonify({'message': 'Email not match...'})
    # Process the data as needed (e.g., save to database)


if __name__ == "__main__":
    # app.run(debug=True)
    ipAddr = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    filename = '../server/ip.json'

    with open(filename, 'r') as f:
        data = json.load(f)

    # print(data['IP'][0]['address'])
    data['IP'][0]['address'] = ipAddr

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(os.listdir(os.getcwd()))
    app.run(debug=False, host = '0.0.0.0', port=80)


# folder_path = 'D:\\mysite\\College_site\\perfect-learn\\server\\notes'

# # Get the list of file names in the folder
# file_names = os.listdir(folder_path)
# print(file_names)
