// dom
const recordButton = document.querySelector(".record-button")
const stopButton = document.querySelector(".stop-button")
//const downloadButton = document.querySelector(".download-button")
const previewPlayer = document.querySelector("#preview")

var question_number=document.querySelector("h2#title>span").innerHTML
document.querySelector("h2#title>span").innerHTML=question_number-1


navigator.mediaDevices.getUserMedia({ audio: true, video: true }).then(recorder);
navigator.mediaDevices.getUserMedia({ audio: true, video: true }).then(stream =>
previewPlayer.srcObject = stream);


// codecs=opus

function recorder(stream) {
    // if (MediaRecorder.isTypeSupported('audio/webm;codecs=opus') == true)
    const options = {
        audioBitsPerSecond: 128000,
        mimeType: 'video/webm'
    };
    const mediaRecorder = new MediaRecorder(stream, options);

    const recordedChunks = [];

    mediaRecorder.addEventListener('dataavailable', function (e) {
        if (e.data.size > 0) { recordedChunks.push(e.data); }
    });

//    mediaRecorder.addEventListener('stop', function () {
//         let blob = new Blob(recordedChunks, { 'type': 'video/mp4' });
//         let video = document.querySelector('#preview');
//         video.src = window.URL.createObjectURL(blob);
//         video.href = URL.createObjectURL(blob);
//         console.log(video.href);
//    });

//    mediaRecorder.addEventListener('stop', function () {
//    let blob = new Blob(recordedChunks);
//
//    // upload file
//    let formdata = new FormData();
//    formdata.append("fname", "video.webm");
//    formdata.append("data", blob);
//
//    let xhr = new XMLHttpRequest();
//    xhr.open("POST", "/upload", false);
//    xhr.send(formdata);
//});

    mediaRecorder.addEventListener('stop', function () {
        let blob = new Blob(recordedChunks);

        // download file
        let aElm = document.createElement('a');
        aElm.href = URL.createObjectURL(blob);
        aElm.download = 'video.webm';
        aElm.click();
    });

    recordButton.onclick = () => { startTimer(); mediaRecorder.start(); };
    stopButton.onclick = () => { stopTimer(); mediaRecorder.stop(); };
};




// 면접 시작 버튼 눌렀을 때
//function videoStart(){
//consol.log("")
//};

// 면접 종료 버튼 눌렀을 때
//function stopRecording() {
//consol.log("")
//};


//event
//recordButton.addEventListener("click", videoStart);
//stopButton.addEventListener("click", stopRecording);

//playButton.addEventListener("click", playRecording);
//testButton.addEventListener("click", testRecording);

