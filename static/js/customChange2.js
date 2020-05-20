function load(){
    var statusNO = 1;

    var imgNO = document.getElementById("image01");
    var txtNO = document.getElementById("text01");

    var imgStatus1 = '{% static "img/status1.jpg" %}';
    //var imgStatus1 = "status1.jpg";
    //var imgStatus1=""{% static "img/work_or_sabori_change.png"%}""
    var txtStatus1 = "勤務開始!今日も一日頑張ろ"
    var imgStatus2 = "status2.jpg";
    var txtStatus2 = "大丈夫?このままだと間に合わないかも..."
    var imgStatus3 = "status3.jpg";
    var txtStatus3 = "お疲れ様!よく頑張ったね!"
    var imgStatus4 = "status4.jpg";
    var txtStatus4 = "働きすぎ!?休憩もしっかりね!"

    if (statusNO == 2){
        imgNO.src = imgStatus2;
        txtNO.innerHTML = txtStatus2;
    }else
        if (statusNO == 3){
            imgNO.src = imgStatus3;
            txtNO.innerHTML = txtStatus3;
        }else
            if (statusNO == 4){
                imgNO.src = imgStatus4;
                txtNO.innerHTML = txtStatus4;
            }else{
                imgNO.src = imgStatus1;
                txtNO.innerHTML = txtStatus1;
            }

}
