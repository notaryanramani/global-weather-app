import subprocess

def download_data(base_dir="scripts"):
    try:
        subprocess.run(["bash", f"{base_dir}/data.sh"])
        return True
    except Exception as e:
        return str(e)
    
def start_kafka_server(base_dir="scripts"):
    try:
        subprocess.run(["bash", f"{base_dir}/kafka.sh"])
        return True
    except Exception as e:
        return str(e)
    