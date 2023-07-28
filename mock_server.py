from flask import Flask, jsonify, Response, stream_with_context
import configparser
import os

app = Flask(__name__)


config = configparser.ConfigParser()
config.read('config.ini')

response_files = {
    '/api/node/class/l2BD.json': config.get('server', 'l2BD_response_file'),
    '/api/node/class/vxlanCktEp.json': config.get('server', 'vxlanCktEp_response_file'),
    '/api/node/class/vlanCktEp.json': config.get('server', 'vlanCktEp_response_file'),
    '/api/node/class/fvCtx.json': config.get('server', 'fvCtx_response_file'),
    '/api/node/class/fvBD.json': config.get('server', 'fvBD_response_file'),
    '/api/node/class/fvAEPg.json': config.get('server', 'fvAEPg_response_file')
}

def read_response_from_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(102400) 
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        print(f"Error: Response file '{file_path}' not found.")
        yield None
    except IOError as e:
        print(f"Error: Unable to read file. {e}")
        yield None

@app.route('/api/node/class/l2BD.json', methods=['GET'])
def get_l2BD_response():
    response_file = response_files.get('/api/node/class/l2BD.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

    
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')

@app.route('/api/node/class/vxlanCktEp.json', methods=['GET'])
def get_vxlanCktEp_response():
    response_file = response_files.get('/api/node/class/vxlanCktEp.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

   
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')
    
@app.route('/api/node/class/vlanCktEp.json', methods=['GET'])
def get_vlanCktEp_response():
    response_file = response_files.get('/api/node/class/vlanCktEp.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

   
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')

@app.route('/api/node/class/fvCtx.json', methods=['GET'])
def get_fvCtx_response():
    response_file = response_files.get('/api/node/class/fvCtx.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

   
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')
    
@app.route('/api/node/class/fvBD.json', methods=['GET'])
def get_fvBD_response():
    response_file = response_files.get('/api/node/class/fvBD.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

   
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')

@app.route('/api/node/class/fvAEPg.json', methods=['GET'])    
def get_fvAEPg_response():
    response_file = response_files.get('/api/node/class/fvAEPg.json')
    if not response_file or not os.path.exists(response_file):
        return jsonify({'error': 'Response file not found'}), 404

   
    return Response(stream_with_context(read_response_from_file(response_file)), content_type='application/json')
    
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'Invalid route'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
