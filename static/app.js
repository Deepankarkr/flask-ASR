document.addEventListener("DOMContentLoaded", function() {
    URL = window.URL || window.webkitURL;
    var gumStream;
    var rec;
    var input;
    var AudioContext = window.AudioContext || window.webkitAudioContext;
    var audioContext
    
    var recordButton = document.getElementById("recordButton");
    var stopButton = document.getElementById("stopButton");
    
    recordButton.addEventListener("click", startRecording);
    stopButton.addEventListener("click", stopRecording);
    });
    function startRecording() {
        console.log("recordButton clicked");
        var constraints = { audio: true, video:false }
        recordButton.disabled = true;
        stopButton.disabled = false;
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
            console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
            audioContext = new AudioContext();
            gumStream = stream;
            input = audioContext.createMediaStreamSource(stream);
            //rec = new Recorder(input,{numChannels:1})
            rec = new Recorder(input, {
              numChannels: 1,
              mimeType: 'audio/wav',
              codec: 'pcm'
            });
            rec.record()
            console.log("Recording started");
        }).catch(function(err) {
            recordButton.disabled = false;
            stopButton.disabled = true;
        });
    }
    
    function stopRecording() {
        console.log("stopButton clicked");
        stopButton.disabled = true;
        recordButton.disabled = false;
        rec.stop();
        gumStream.getAudioTracks()[0].stop();
        rec.exportWAV(createDownloadLink);
    }
    
    function createDownloadLink(blob) {
        var filename = "recording.wav";
        var xhr = new XMLHttpRequest();
        xhr.onload = function(e) {
            if (this.readyState === 4) {
                console.log("Server returned:", e.target.responseText);
            }};
        var fd = new FormData();
        fd.append("audio_data", blob, filename);
        xhr.open("POST", "http://127.0.0.1:3000/recording", true);
        xhr.send(fd);
    }
    