const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth();
const currentDay = new Date().getDate();
const currentOfWeek = new Date().getDay();
const TodayDate = miladi_be_shamsi(currentYear, currentMonth+1, currentDay);
let ThisMonth;
function miladi_be_shamsi(gy, gm, gd) {
    var g_d_m, jy, jm, jd, gy2, days;
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    gy2 = (gm > 2) ? (gy + 1) : gy;
    days = 355666 + (365 * gy) + ~~((gy2 + 3) / 4) - ~~((gy2 + 99) / 100) + ~~((gy2 + 399) / 400) + gd + g_d_m[gm - 1];
    jy = -1595 + (33 * ~~(days / 12053));
    days %= 12053;
    jy += 4 * ~~(days / 1461);
    days %= 1461;
    if (days > 365) {
      jy += ~~((days - 1) / 365);
      days = (days - 1) % 365;
    }
    if (days < 186) {
      jm = 1 + ~~(days / 31);
      jd = 1 + (days % 31);
    } else {
      jm = 7 + ~~((days - 186) / 30);
      jd = 1 + ((days - 186) % 30);
    }
    return [jy, jm, jd];
}
function shamsi_be_miladi(jy, jm, jd) {
    var sal_a, gy, gm, gd, days;
    jy += 1595;
    days = -355668 + (365 * jy) + (~~(jy / 33) * 8) + ~~(((jy % 33) + 3) / 4) + jd + ((jm < 7) ? (jm - 1) * 31 : ((jm - 7) * 30) + 186);
    gy = 400 * ~~(days / 146097);
    days %= 146097;
    if (days > 36524) {
      gy += 100 * ~~(--days / 36524);
      days %= 36524;
      if (days >= 365) days++;
    }
    gy += 4 * ~~(days / 1461);
    days %= 1461;
    if (days > 365) {
      gy += ~~((days - 1) / 365);
      days = (days - 1) % 365;
    }
    gd = days + 1;
    sal_a = [0, 31, ((gy % 4 === 0 && gy % 100 !== 0) || (gy % 400 === 0)) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    for (gm = 0; gm < 13 && gd > sal_a[gm]; gm++) gd -= sal_a[gm];
    return `${gy}-${gm}-${gd}`;
}
function LoadCalendar(yy, mm, dd){
    document.getElementById("CurrentYear").textContent = yy;
    switch (mm) {
        case 1:
            ThisMonth = "فروردین"
            break;
        case 2:
            ThisMonth = "اردیبهشت"
            break;
        case 3:
            ThisMonth = "خرداد"
            break;
        case 4:
            ThisMonth = "تیر"
            break;
        case 5:
            ThisMonth = "مرداد"
            break;
        case 6:
            ThisMonth = "شهریور"
            break;
        case 7:
            ThisMonth = "مهر"
            break;
        case 8:
            ThisMonth = "آبان"
            break;
        case 9:
            ThisMonth = "آذر"
            break;
        case 10:
            ThisMonth = "دی"
            break;
        case 11:
            ThisMonth = "بهمن"
            break;
        case 12:
            ThisMonth = "اسفند"
            break;
    }
    document.getElementById("CurrentMonth").textContent = ThisMonth;

    const CalBody = document.getElementById("CalBody");
    function CalculateDay(x, y, z){
        // let a = TodayDate[2]%7;
        // return currentOfWeek-a+1;
        const miladi = shamsi_be_miladi(x, y, z);
        const a = new Date(miladi).getDay();
        if(a==6){return 1;}
        else{return -a;}
    }
    let day = CalculateDay(yy, mm, 1);
    for(let i = 0 ; i < 5 ; i++){
        const CalRow = document.createElement("tr");
        CalRow.className = "Row";
        for(let j = 0 ; j < 7 ; j++){
            const CalCell = document.createElement("td");
            CalCell.innerHTML = day;
            CalCell.id = `${i}`+`${j}`;
            if(day < 1 || day > 30){
                CalCell.style.color = "rgba(0,0,0,0)";
            }
            if(day == dd){
                CalCell.style.backgroundColor = "#F2F4F3";
                CalCell.style.color = "#21333B";
            }
            CalRow.appendChild(CalCell);
            day++;
        }
        CalRow.id = `${i}`;
        CalBody.appendChild(CalRow);
    }
}
function ShowChangingForm(){
    document.getElementById("ChangingFormParent").style.display = "flex";
}
function HideChangingForm(){
    document.getElementById("ChangingFormParent").style.display = "none";
}
function LoadFromThis(){
    const y = Number(document.getElementById("ThisYear").value);
    const m = Number(document.getElementById("ThisMonth").value);
    if(y<1300 || y>2000 || m>12 || m<1){
        alert("مقدار ماه یا سال معتبر نمی‌باشد.");
    }
    else{
        let rows = document.querySelectorAll(".Row");
        console.log(rows[4]);
        for (let i = 0 ; i < rows.length ; i++){
            rows[i].remove();
            console.log(i);
        }
        LoadCalendar(y, m, 1);
        HideChangingForm();
    }
}
LoadCalendar(TodayDate[0], TodayDate[1], TodayDate[2]);