from flask import Flask, render_template, request, redirect, url_for
import os
import magic

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

        # Validate file extension
        if not pdf_file.filename.endswith('.pdf'):
            return render_template('upload.html', error='Invalid file format. Please upload a PDF file.')

        # Validate file size
        max_size = 5 * 1024 * 1024  # 5 MB
        if len(pdf_file.read()) > max_size:
            return render_template('upload.html', error='File size exceeds the limit. Please upload a file up to 5 MB.')

        # Reset file cursor to the beginning for saving
        pdf_file.seek(0)

        # Validate file content using magic module
        file_content = pdf_file.read()
        mime_type = magic.from_buffer(file_content, mime=True)
        if mime_type != 'application/pdf':
            return render_template('upload.html', error='Invalid file format. Please upload a valid PDF file.')

        # Save the file to a specific folder
        upload_folder = './uploads'  # Replace with the desired folder path
        pdf_file.seek(0)
        pdf_file.save(os.path.join(upload_folder, pdf_file.filename))

        # Redirect to a success page or perform further processing
        return redirect(url_for('success'))

    # If it's a GET request, render the upload page
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
