from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define route for success page
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file from the form
        pdf_file = request.files['pdf_file']

        # Save the file to a specific folder
        upload_folder = './uploads'  # Replace with the desired folder path
        pdf_file.save(os.path.join(upload_folder, pdf_file.filename))

        # Redirect to a success page or perform further processing
        return redirect(url_for('success'))

    # If it's a GET request, render the upload page
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
