pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                echo "Creando entorno virtual..."
                bat '"C:\\Users\\quisp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.12\\Python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar script') {
            steps {
                echo "Ejecutando script principal..."
                bat 'venv\\Scripts\\activate && python hola2.py'
            }
        }
    }

    post {
        success { echo "✅ Pipeline completado con éxito" }
        failure { echo "❌ Error en alguna etapa del pipeline" }
    }
}
