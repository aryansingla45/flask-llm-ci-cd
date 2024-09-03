// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const pipelineTypeSelect = document.getElementById('pipeline_type');
    const fileInput = document.getElementById('file');

    pipelineTypeSelect.addEventListener('change', function() {
        const selectedType = this.value;
        let acceptTypes = '';

        switch(selectedType) {
            case 'yaml':
                acceptTypes = '.yaml,.yml';
                break;
            case 'docker':
                acceptTypes = '.Dockerfile,.dockerfile,Dockerfile';
                break;
            case 'jenkins':
                acceptTypes = '.Jenkinsfile,.jenkinsfile,Jenkinsfile';
                break;
            // Add more cases as needed
            default:
                acceptTypes = '';
        }

        fileInput.setAttribute('accept', acceptTypes);
    });
});
