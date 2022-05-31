from google.api_core.client_options import ClientOptions
from googleapiclient import discovery


app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    userid = request.form.get('userid')
    endpoint = 'https://asia-southeast1-ml.googleapis.com/'
    client_options = ClientOptions(api_endpoint=endpoint)
    ml = discovery.build('ml', 'v1', client_options=client_options)

    request_body = { 'instances': [{"input_1": "32"}] }
    request = ml.projects().predict(
        name='projects/delta-essence-349912/models/cobamodel/versions/versi2',
        body=request_body)

    response = request.execute()
    print(response)
if __name__ == '__main__':
    app.run(debug=True)