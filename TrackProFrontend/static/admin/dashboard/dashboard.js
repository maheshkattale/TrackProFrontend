$(document).ready(function() {
    const todaysFullDate = getTodaysDate();
    $("#todayDate").text(todaysFullDate);

    // createFilteredArray();

    // createPagination();

    // populateTable();
});

$(".dark-overlay").click(function() {
    closeExpandedNav();
});

$('#hamburger-icon').click(function() {
    $(".expanded-nav").addClass("expanded");
    $(".dark-overlay").show();
})

function closeExpandedNav() {
    $(".expanded-nav").removeClass("expanded");
    setTimeout(() => {
        $(".dark-overlay").hide();
    }, 480);
}

function getTodaysDate() {
    const date = new Date();
    const day = date.getDay();
    let todayDay;

    if (day == 0) {
        todayDay = "Sunday";
    } else if (day == 1) {
        todayDay = "Monday";
    } else if (day == 2) {
        todayDay = "Tuesday";
    } else if (day == 3) {
        todayDay = "Wednesday";
    } else if (day == 4) {
        todayDay = "Thursday";
    } else if (day == 5) {
        todayDay = "Friday";
    } else {
        todayDay = "Saturday";
    }

    const today =
        todayDay +
        ", " +
        date.getDate() +
        "/" +
        (date.getMonth() + 1) +
        "/" +
        date.getFullYear();

    return today;
}

function getTime() {
    const date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let currentTime = hours + " : " + minutes;

    return currentTime;
}

function checkInOut() {
    let ioBtn = $("#IOBtn");
    let innerText = ioBtn.text().trim();
    let iBtn = $(".Itime b");
    let oBtn = $(".Otime b");

    if (innerText == "Check In") {
        iBtn.text(getTime());
        iBtn.css("color", "#3DAB45");
        ioBtn.text("Check Out");
        ioBtn.css("backgroundColor", "#F24B59");
    }

    if (innerText == "Check Out") {
        oBtn.text(getTime());
        oBtn.css("color", "#F24B59");
        ioBtn.prop("disabled", "true");
        ioBtn.css("backgroundColor", "#BFBFBF");

        $("#totalHours").text(workingHours(iBtn.text(), oBtn.text()));
        $("#totalHours").css("color", "#174fa3");
    }
}

function workingHours(inTime, outTime) {
    let inHours = parseInt(inTime.substr(0, 2));
    let inMins = parseInt(inTime.substr(5, 2));
    let inTotTime = inHours * 60 + inMins;

    let outHours = parseInt(outTime.substr(0, 2));
    let outMins = parseInt(outTime.substr(5, 2));
    let outTotTime = outHours * 60 + outMins;

    let totalTimeWorked = outTotTime - inTotTime;

    let hoursWorked = Math.floor(totalTimeWorked / 60);
    let minsWorked = totalTimeWorked - hoursWorked * 60;

    if (hoursWorked < 10) {
        hoursWorked = "0" + hoursWorked;
    }

    if (minsWorked < 10) {
        minsWorked = "0" + minsWorked;
    }

    let timeWorkedString = hoursWorked + "h " + minsWorked + "m";

    return timeWorkedString;
}

$("#taskResume").click(function() {
    $(this).toggleClass("resumed");
});

// =========================Attendance Graph============================

// const ctx = document.getElementById("attendanceGraph").getContext("2d");

// let gradient = ctx.createLinearGradient(0, 0, 0, 150);
// gradient.addColorStop(0, "rgba(0, 176, 239, 0.5)");
// gradient.addColorStop(1, "rgba(0, 176, 239, 0.1)");

// const scale =
//     $(".attendanceGraphWrapper").width() / $(".attendanceGraphWrapper").height();

// let currMonth = "Nov";
// let monthView = true;

// let monthlyAttendance = [
//     { date: 1, attendance: 75 },
//     { date: 2, attendance: 77 },
//     { date: 3, attendance: 82 },
//     { date: 4, attendance: 79 },
//     { date: 5, attendance: 77 },
//     { date: 6, attendance: 78 },
//     { date: 7, attendance: 86 },
//     { date: 8, attendance: 84 },
//     { date: 9, attendance: 78 },
//     { date: 10, attendance: 76 },
//     { date: 11, attendance: 80 },
//     { date: 12, attendance: 83 },
//     { date: 13, attendance: 78 },
//     { date: 14, attendance: 83 },
//     { date: 15, attendance: 87 },
//     { date: 16, attendance: 82 },
//     { date: 17, attendance: 81 },
//     { date: 18, attendance: 78 },
//     { date: 19, attendance: 82 },
//     { date: 20, attendance: 85 },
//     { date: 21, attendance: 86 },
//     { date: 22, attendance: 87 },
//     { date: 23, attendance: 80 },
//     { date: 24, attendance: 82 },
//     { date: 25, attendance: 78 },
//     { date: 26, attendance: 78 },
//     { date: 27, attendance: 82 },
//     { date: 28, attendance: 88 },
//     { date: 29, attendance: 80 },
//     { date: 30, attendance: 78 },
//     { date: 31, attendance: 78 },
// ];

// let datesArr = monthlyAttendance.map((day) => day.date);
// let attendanceArr = monthlyAttendance.map((day) => day.attendance);

// const myChart = new Chart(ctx, {
//     type: "line",
//     options: {
//         aspectRatio: scale,
//         responsive: true,
//         plugins: {
//             legend: {
//                 display: false,
//             },
//             tooltip: {
//                 backgroundColor: "#7F989E",
//                 titleColor: "#CFCFCF",
//                 titleAlign: "center",
//                 bodyColor: "#fff",
//                 bodyAlign: "center",
//                 displayColors: false,
//                 position: "nearest",
//                 callbacks: {
//                     title: function(context) {
//                         return `${context[0].label} ${currMonth}`;
//                     },
//                 },
//             },
//         },
//         radius: 0,
//         hitRadius: 15,
//         scales: {
//             y: {
//                 max: 100,
//                 min: 50,
//                 ticks: {
//                     stepSize: 10,
//                     color: "#BFBFBF",
//                 },
//                 grid: {
//                     drawBorder: false,
//                 },
//             },

//             x: {
//                 grid: {
//                     display: false,
//                     drawBorder: false,
//                 },
//                 ticks: {
//                     color: "#BFBFBF",
//                     maxTicksLimit: 5,
//                     maxRotation: 0,
//                 },
//             },
//         },
//         label: {
//             display: false,
//         },
//         font: {
//             size: 12,
//         },
//     },
//     data: {
//         labels: datesArr,
//         datasets: [{
//             label: "Attendance",
//             data: attendanceArr,
//             borderColor: "#174fa3",
//             borderWidth: 1.5,
//             fill: true,
//             backgroundColor: gradient,
//             tension: 0.3,
//         }, ],
//     },
// });

// function weekMonthToggle() {
//     if (monthView) {
//         monthlyAttendance = [
//             { date: 19, attendance: 82 },
//             { date: 20, attendance: 85 },
//             { date: 21, attendance: 86 },
//             { date: 22, attendance: 87 },
//             { date: 23, attendance: 80 },
//             { date: 24, attendance: 82 },
//             { date: 25, attendance: 78 },
//         ];

//         $(".attendanceToggle p").text("This Week");
//         monthView = !monthView;
//     } else {
//         monthlyAttendance = [
//             { date: 1, attendance: 75 },
//             { date: 2, attendance: 77 },
//             { date: 3, attendance: 82 },
//             { date: 4, attendance: 79 },
//             { date: 5, attendance: 77 },
//             { date: 6, attendance: 78 },
//             { date: 7, attendance: 86 },
//             { date: 8, attendance: 84 },
//             { date: 9, attendance: 78 },
//             { date: 10, attendance: 76 },
//             { date: 11, attendance: 80 },
//             { date: 12, attendance: 83 },
//             { date: 13, attendance: 78 },
//             { date: 14, attendance: 83 },
//             { date: 15, attendance: 87 },
//             { date: 16, attendance: 82 },
//             { date: 17, attendance: 81 },
//             { date: 18, attendance: 78 },
//             { date: 19, attendance: 82 },
//             { date: 20, attendance: 85 },
//             { date: 21, attendance: 86 },
//             { date: 22, attendance: 87 },
//             { date: 23, attendance: 80 },
//             { date: 24, attendance: 82 },
//             { date: 25, attendance: 78 },
//             { date: 26, attendance: 78 },
//             { date: 27, attendance: 82 },
//             { date: 28, attendance: 88 },
//             { date: 29, attendance: 80 },
//             { date: 30, attendance: 78 },
//             { date: 31, attendance: 78 },
//         ];

//         $(".attendanceToggle p").text("This Month");
//         monthView = !monthView;
//     }

//     datesArr = monthlyAttendance.map((day) => day.date);
//     attendanceArr = monthlyAttendance.map((day) => day.attendance);

//     myChart.data.datasets[0].data = attendanceArr;
//     myChart.data.labels = datesArr;
//     myChart.update();
// }

// $("#viewToggle").click(function() {
//     weekMonthToggle();
// });

/* ======================Events Calendar Card================================== */

var Calendar = function(t) {
    (this.divId = t.RenderID ? t.RenderID : '[data-render="calendar"]'),
    (this.DaysOfWeek = t.DaysOfWeek ?
        t.DaysOfWeek : ["S", "M", "T", "W", "T", "F", "S"]),
    (this.Months = t.Months ?
        t.Months : [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]);
    var e = new Date();
    (this.CurrentMonth = e.getMonth()), (this.CurrentYear = e.getFullYear());
    var r = t.Format;
    this.f = "string" == typeof r ? r.charAt(0).toUpperCase() : "M";
};
(Calendar.prototype.nextMonth = function() {
    11 == this.CurrentMonth ?
        ((this.CurrentMonth = 0), (this.CurrentYear = this.CurrentYear + 1)) :
        (this.CurrentMonth = this.CurrentMonth + 1),
        (this.divId = '[data-active="false"] .render'),
        this.showCurrent();
}),
(Calendar.prototype.prevMonth = function() {
    0 == this.CurrentMonth ?
        ((this.CurrentMonth = 11), (this.CurrentYear = this.CurrentYear - 1)) :
        (this.CurrentMonth = this.CurrentMonth - 1),
        (this.divId = '[data-active="false"] .render'),
        this.showCurrent();
}),
(Calendar.prototype.previousYear = function() {
    (this.CurrentYear = this.CurrentYear - 1), this.showCurrent();
}),
(Calendar.prototype.nextYear = function() {
    (this.CurrentYear = this.CurrentYear + 1), this.showCurrent();
}),
(Calendar.prototype.showCurrent = function() {
    this.Calendar(this.CurrentYear, this.CurrentMonth);
}),
(Calendar.prototype.checkActive = function() {
    1 ==
        document.querySelector(".months").getAttribute("class").includes("active") ?
        document.querySelector(".months").setAttribute("class", "months") :
        document
        .querySelector(".months")
        .setAttribute("class", "months active"),
        "true" == document.querySelector(".month-a").getAttribute("data-active") ?
        (document.querySelector(".month-a").setAttribute("data-active", !1),
            document.querySelector(".month-b").setAttribute("data-active", !0)) :
        (document.querySelector(".month-a").setAttribute("data-active", !0),
            document.querySelector(".month-b").setAttribute("data-active", !1)),
        setTimeout(function() {
            document
                .querySelector(".calendar .header")
                .setAttribute("class", "header active");
        }, 200),
        document
        .querySelector("body")
        .setAttribute(
            "data-theme",
            this.Months[
                document
                .querySelector('[data-active="true"] .render')
                .getAttribute("data-month")
            ].toLowerCase()
        );
}),
(Calendar.prototype.Calendar = function(t, e) {
    "number" == typeof t && (this.CurrentYear = t),
        "number" == typeof t && (this.CurrentMonth = e);
    var r = new Date().getDate(),
        n = new Date().getMonth(),
        a = new Date().getFullYear(),
        o = new Date(t, e, 1).getDay(),
        i = new Date(t, e + 1, 0).getDate(),
        u =
        0 == e ? new Date(t - 1, 11, 0).getDate() : new Date(t, e, 0).getDate(),
        s = "<span>" + this.Months[e] + ", " + t + "</span>",
        d = '<div class="table">';
    d += '<div class="row head">';
    for (var c = 0; c < 7; c++)
        d += '<div class="cell">' + this.DaysOfWeek[c] + "</div>";
    d += "</div>";
    for (
        var h, l = (dm = "M" == this.f ? 1 : 0 == o ? -5 : 2), v = ((c = 0), 0); v < 6; v++
    ) {
        d += '<div class="row">';
        for (var m = 0; m < 7; m++) {
            if ((h = c + dm - o) < 1)
                d += '<div class="cell disable">' + (u - o + l++) + "</div>";
            else if (h > i) d += '<div class="cell disable">' + l++ + "</div>";
            else {
                (d +=
                    '<div class="cell' +
                    (r == h && this.CurrentMonth == n && this.CurrentYear == a ?
                        " active" :
                        "") +
                    '"><span>' +
                    h +
                    "</span></div>"),
                (l = 1);
            }
            c % 7 == 6 && h >= i && (v = 10), c++;
        }
        d += "</div>";
    }
    (d += "</div>"),
    (document.querySelector('[data-render="month-year"]').innerHTML = s),
    (document.querySelector(this.divId).innerHTML = d),
    document
        .querySelector(this.divId)
        .setAttribute("data-date", this.Months[e] + " - " + t),
        document.querySelector(this.divId).setAttribute("data-month", e);
}),
(window.onload = function() {
    var t = new Calendar({
        RenderID: ".render-a",
        Format: "M",
    });
    t.showCurrent(), t.checkActive();
    var e = document.querySelectorAll(".header [data-action]");
    for (i = 0; i < e.length; i++)
        e[i].onclick = function() {
            if (
                (document
                    .querySelector(".calendar .header")
                    .setAttribute("class", "header"),
                    "true" ==
                    document.querySelector(".months").getAttribute("data-loading"))
            )
                return (
                    document
                    .querySelector(".calendar .header")
                    .setAttribute("class", "header active"), !1
                );
            var e;
            document.querySelector(".months").setAttribute("data-loading", "true"),
                this.getAttribute("data-action").includes("prev") ?
                (t.prevMonth(), (e = "left")) :
                (t.nextMonth(), (e = "right")),
                t.checkActive(),
                document.querySelector(".months").setAttribute("data-flow", e),
                document
                .querySelector('.month[data-active="true"]')
                .addEventListener("webkitTransitionEnd", function() {
                    document.querySelector(".months").removeAttribute("data-loading");
                }),
                document
                .querySelector('.month[data-active="true"]')
                .addEventListener("transitionend", function() {
                    document.querySelector(".months").removeAttribute("data-loading");
                });
        };
});

const calendarView1 = $(".calendarview1");
const calendarView2 = $(".calendarview2");
const calendar = $(".calendar");

calendarView1.click(function() {
    calendarView1.addClass("calViewSelected");
    calendarView2.removeClass("calViewSelected");
    calendar.show();
});

calendarView2.click(function() {
    calendarView2.addClass("calViewSelected");
    calendarView1.removeClass("calViewSelected");
    calendar.hide();
});

// =====================================DATATABLE CARD==========================================
// let employeeData = {
//         { dashboard.topfive }
//     }
// let employeeData = [
//   {
//     id: 87,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 85,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 65,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 101,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 23,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 5,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 45,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 71,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 37,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 91,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 98,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 119,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
//   {
//     id: 17,
//     name: "Rushabh",
//     lastName: "Anam",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "180%",
//     status: "present",
//   },

//   {
//     id: 25,
//     name: "Divya",
//     lastName: "Sheth",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_2.png",
//     designation: "Sr. Frontend Developer",
//     department: "Frontend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "150%",
//     status: "present",
//   },

//   {
//     id: 48,
//     name: "Divyam",
//     lastName: "Shah",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_1.png",
//     designation: "Sr. Backend Developer",
//     department: "Backend",
//     checkInTime: "09:15",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "wfh",
//   },

//   {
//     id: 36,
//     name: "Jash",
//     lastName: "Patel",
//     profileImage: "./Media/TrackProRankingCard/profile_picture_3.png",
//     designation: "Sr. Backend Developer",
//     department: "Admin",
//     checkInTime: "-- : --",
//     checkOutTime: "-- : --",
//     trackproScore: "123%",
//     status: "leave",
//   },
// ];

// let filteredData = [];
// let filterValue = 1;
// let noOfPages = 1;
// let currentPage = 1;

// $(".filterBtn").click(function() {
//     // console.log($(this).attr('value'));
//     $("#searchQuery").val("");
//     filterValue = $(this).attr("value");
//     addNotSelected();
//     $(this).removeClass("notSelected");

//     createFilteredArray();

//     createPagination();

//     currentPage = 1;

//     clearTable();

//     populateTable();

// });

// function addNotSelected() {
//     $(".filterBtn").each(function() {
//         $(this).addClass("notSelected");
//     });
// }

// function createFilteredArray() {
//     if (filterValue == 1) {
//         filteredData = employeeData.slice();
//     } else if (filterValue == 2) {
//         filteredData = employeeData.filter(function(employee) {
//             if (employee.status == "present") {
//                 return employee;
//             }
//         });
//     } else if (filterValue == 3) {
//         filteredData = employeeData.filter(function(employee) {
//             if (employee.status == "leave") {
//                 return employee;
//             }
//         });
//     } else if (filterValue == 4) {
//         filteredData = employeeData.filter(function(employee) {
//             if (employee.status == "wfh") {
//                 return employee;
//             }
//         });
//     }

//     // console.log(filteredData);
// }

// function clearTable() {
//     $(".tablerow").each(function() {
//         $(this).detach();
//     });
// }

// function createPagination() {
//     noOfPages = Math.floor(filteredData.length / 7) + 1;
// }

// function populateTable() {
//     filteredData.forEach(function(row, i) {
//         let rowString = `<tr class="tablerow" id="${i + 1}">
//     <td>
//       <div class="employeeDetails">
//         <div class="statusDot d-none d-lg-block"></div>
//         <div class="tableProfileImage" style="background-image:url(${
//           row.profileImage
//         })"></div>
//         <div class="employeeNameAndDesignation">
//           <p class="empName">${row.name} ${row.lastName}</p>
//           <p class="empDesig d-none d-lg-block">${row.designation}</p>
//         </div>
//       </div> 
//     </td>
//     <td>${row.department}</td>
//     <td>${row.checkInTime}</td>
//     <td>${row.checkOutTime}</td>
//     <td class="tableTrackProScore d-none d-lg-table-cell">${row.trackproScore}</td>
//   </tr>`;

//         if (row.status == "leave") {
//             rowString = `<tr class="tablerow" id="${i + 1}">
//     <td>
//       <div class="employeeDetails">
//         <div class="statusDot red d-none d-lg-block"></div>
//         <div class="tableProfileImage redBorder" style="background-image:url(${
//           row.profileImage
//         })"></div>
//         <div class="employeeNameAndDesignation">
//           <p class="empName">${row.name} ${row.lastName}</p>
//           <p class="empDesig d-none d-lg-block">${row.designation}</p>
//         </div>
//       </div> 
//     </td>
//     <td>${row.department}</td>
//     <td>${row.checkInTime}</td>
//     <td>${row.checkOutTime}</td>
//     <td class="tableTrackProScore d-none d-lg-table-cell">${row.trackproScore}</td>
//   </tr>`;
//         }

//         if (row.status == "wfh") {
//             rowString = `<tr class="tablerow" id="${i + 1}">
//     <td>
//       <div class="employeeDetails">
//         <div class="statusDot yellow d-none d-lg-block"></div>
//         <div class="tableProfileImage yellowBorder" style="background-image:url(${
//           row.profileImage
//         })"></div>
//         <div class="employeeNameAndDesignation">
//           <p class="empName">${row.name} ${row.lastName}</p>
//           <p class="empDesig d-none d-lg-block">${row.designation}</p>
//         </div>
//       </div> 
//     </td>
//     <td>${row.department}</td>
//     <td>${row.checkInTime}</td>
//     <td>${row.checkOutTime}</td>
//     <td class="tableTrackProScore d-none d-lg-table-cell">${row.trackproScore}</td>
//   </tr>`;
//         }

//         if (i < currentPage * 7 && i >= (currentPage - 1) * 7) {
//             $(".datatable").append(rowString);
//         }
//     });

//     updatePagination();
// }

// $("#tableSearchButton").click(function() {

//     addNotSelected();

//     let searchString = $("#searchQuery").val().toLowerCase();

//     if (!searchString) {
//         console.log("doesNotExist");
//     } else {
//         currentPage = 1;

//         filteredData = employeeData.filter(function(employee) {
//             if (
//                 employee.name.toLowerCase().includes(searchString) ||
//                 employee.lastName.toLowerCase().includes(searchString) ||
//                 employee.department.toLowerCase().includes(searchString)
//             ) {
//                 return employee;
//             }
//         });

//         createPagination();

//         clearTable();

//         populateTable();

//     }
// });

// function updatePagination() {

//     let rowRange = ((currentPage - 1) * 7) + 1;
//     let currentPageString;

//     let displayedResults = "Showing " + rowRange + " to " + (rowRange + $(".tablerow").length - 1) + " of " + filteredData.length + " results";
//     $('.showingResults').text(displayedResults);

//     if (currentPage < 10) {
//         currentPageString = "0" + currentPage;
//     }
//     $(".currentPage").text(currentPageString);

//     $('.totalPages').text("of " + noOfPages);
// }

// $(".prevPage").click(function() {

//     if (currentPage > 1) {
//         currentPage -= 1;

//         clearTable();

//         populateTable();
//     }
// })

// $(".nextPage").click(function() {

//     if (currentPage < noOfPages) {
//         currentPage += 1;

//         clearTable();

//         populateTable();
//     }
// })