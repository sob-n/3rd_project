// dom


const recordButton = document.querySelector(".record-button")
const stopButton = document.querySelector(".stop-button")
const playButton = document.querySelector(".play-button")
const downloadButton = document.querySelector(".download-button")
const previewPlayer = document.querySelector("#preview")
const recordingPlayer = document.querySelector("#recording")

const testButton = document.querySelector('.test-button')

let recorder;
let recordedChunks = [];
//functions
function videoStart(){
    navigator.mediaDevices.getUserMedia({ video: true, audio: true })
        .then(stream => {
            previewPlayer.srcObject = stream;
            startRecording(previewPlayer.captureStream())

        })

}
//function videoStart(){
//    navigator.mediaDevices.getUserMedia(constraintObj)
//        .then(function(mediaStreamObj) {
//            //connect the media stream to the first video element
//            let video = document.querySelector('video');
//            if ("srcObject" in video) {
//                video.srcObject = mediaStreamObj;
//            } else {
//                //old version
//                video.src = window.URL.createObjectURL(mediaStreamObj);
//            }
//}
function startRecording(stream) {
    recordedChunks = [];
    const recorder = new MediaRecorder(stream);
    recorder.ondataavailable = (e) => { recordedChunks.push(e.data)}
    recorder.start()
}
function stopRecording() {
    previewPlayer.srcObject.getTracks().forEach(track => track.stop());
    recorder.stop()
}
function testRecording() {
//    const output =execSync('ls', {encoding: 'utf-8'});
//
//    console.log(os.system('ls'))
//    os.system('ls')
//    document.getElementById('')
    txt = navigator.platform
    alert(txt)
}

function playRecording() {
    const recordedBlob = new Blob(recordedChunks, {type: "video/webm"});
    recordingPlayer.src = URL.createObjectURL(recordedBlob);
    recordingPlayer.play();
    downloadButton.href = recordingPlayer.src;
    downloadButton.download = 'recording_${new Date()}.webm';
    console.log(recordingPlayer.src)
}


//event
recordButton.addEventListener("click", videoStart);
stopButton.addEventListener("click", stopRecording);
playButton.addEventListener("click", playRecording);
testButton.addEventListener("click", testRecording);

