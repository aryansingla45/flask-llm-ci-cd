document.getElementById('uploadForm').addEventListener('submit', function(event) {
    const pipelineType = document.getElementById('pipeline_type').value;
    const file = document.getElementById('file').files[0];

    if (!pipelineType || !file) {
        alert('Please select a pipeline type and upload a file.');
        event.preventDefault();
        return;
    }

    const fileExtension = file.name.split('.').pop().toLowerCase();
    const pipelineFileMapping = {
        'yaml': ['yaml', 'yml'],
        'docker': ['dockerfile'],
        'jenkins': ['jenkinsfile'],
        'travis': ['travis.yml'],
        'github_actions': ['yml', 'yaml']
    };

    if (!pipelineFileMapping[pipelineType].includes(fileExtension)) {
        alert('Invalid file format for the selected pipeline type.');
        event.preventDefault();
    }
});
