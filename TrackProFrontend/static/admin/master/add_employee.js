$("#addEmpRole").select2();
$("#addEmpDesignation").select2();
$("#addEmpDepartment").select2();
$("#addEmpEmploymentStatus").select2();
$("#addEmpLocation").select2();
$("#addEmpTOW").select2();

$("#addEmpJoinDate").datepicker({
    dateFormat: 'dd-mm-yy',
    maxDate: 0 ,
    changeYear:true,
    yearRange: "-100:+0",
    changeMonth: true,
});

$("#addEmpJoinDate2").datepicker({
    dateFormat: 'dd-mm-yy',
    maxDate:"-18Y",
    changeYear:true,
    yearRange: "-100:+0",
    changeMonth: true,

});

$(document).on('select2:open', () => {
    document.querySelector('.select2-search__field').focus();
});

let passwordVisible = false;
let passwordInputField = $('#addEmpPassword');
let passwordEye = $('#passwordToggle');

$('#passwordToggle').click(function() {

    passwordEye.toggleClass('passwordVisible');

    if (passwordVisible) {
        passwordInputField.attr('type', 'password');
        passwordVisible = !passwordVisible;
    } else {
        passwordInputField.attr('type', 'text');
        passwordVisible = !passwordVisible;
    }
})

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

function editformValidation() {
    var regex = /[A-Za-z0-9_~\-!@#\$%\^&\*\(\)]+$/;
    var addEmpFirstname = $('#addEmpFirstname').val().trim();
    var addEmpLastname = $('#addEmpLastname').val().trim();
    var addEmpEmailId = $('#addEmpEmailId').val().trim();
    var addEmpDesignation = $('#addEmpDesignation').val().trim();
    var addEmpEmploymentStatus = $('#addEmpEmploymentStatus').val();
    var addEmpLocation = $('#addEmpLocation').val();
    var addEmpMobileNumber = $('#addEmpMobileNumber').val();
    var addEmpRole = $('#addEmpRole').val();
    var addEmpDepartment = $('#addEmpDepartment').val();
    var addEmpJoinDate = $('#addEmpJoinDate').val();
    var addEmpTOW = $('#addEmpTOW').val();

    if (IsValid(addEmpFirstname)) {
     
        $('#addEmpFirstname_err').show().delay(3000).slideUp();
        $('#addEmpFirstname_err').html('First Name is required');
        $('#addEmpFirstname').focus();
        return false;
    } else if (IsValid(addEmpLastname)) {
      
        $('#addEmpLastname_err').show().delay(3000).slideUp();
        $('#addEmpLastname_err').html('Last Name is required');
        $('#addEmpLastname').focus();
        return false;
    }else if (!validateEmail(addEmpEmailId)) {
      
        $('#addEmpEmailId_err').show().delay(3000).slideUp();
        $('#addEmpEmailId_err').html('Invalid Email');
        $('#addEmpEmailId').focus();
        return false;
    } else if (IsValid(addEmpDesignation)) {
      
        $('#addEmpDesignation_err').show().delay(3000).slideUp();
        $('#addEmpDesignation_err').html('Designation field is required');
        $('#addEmpDesignation').focus();
        return false;
    } else if (IsValid(addEmpEmploymentStatus)) {
      
        $('#addEmpEmploymentStatus_err').show().delay(3000).slideUp();
        $('#addEmpEmploymentStatus_err').html('Please select Employee Status');
        $('#addEmpEmploymentStatus').focus();
        return false;
    } else if (IsValid(addEmpLocation)) {
       
        $('#addEmpLocation_err').show().delay(3000).slideUp();
        $('##addEmpLocation_err').html('Please select location');
        $('#addEmpLocation').focus();
        return false;
    } else if (IsValid(addEmpMobileNumber)) {
       
        $('#addEmpMobileNumber_err').show().delay(3000).slideUp();
        $('#addEmpMobileNumber_err').html('Please provide mobile number');
        $('#addEmpMobileNumber').focus();
        return false;
    } else if (addEmpMobileNumber.length != 10) {
       
        $('#addEmpMobileNumber_err').show().delay(3000).slideUp();
        $('#addEmpMobileNumber_err').html('Mobile Number should be of 10 digits');
        $('#addEmpMobileNumber').focus();
        return false;
    } else if (IsValid(addEmpRole)) {
       
        $('#addEmpRole_err').show().delay(3000).slideUp();
        $('#addEmpRole_err').html('Please select Role');
        $('#addEmpRole').focus();
        return false;
    } else if (IsValid(addEmpDepartment)) {
       
        $('#addEmpDepartment_err').show().delay(3000).slideUp();
        $('#addEmpDepartment_err').html('Please select Department');
        $('#addEmpDepartment').focus();
        return false;
    } else if (IsValid(addEmpJoinDate)) {
       
        $('#addEmpJoinDate_err').show().delay(3000).slideUp();
        $('#addEmpJoinDate_err').html('Please provide joining date');
        $('#addEmpJoinDate').focus();
        return false;
    } else if (IsValid(addEmpTOW)) {
      
        $('#addEmpTOW_err').show().delay(3000).slideUp();
        $('#addEmpTOW_err').html('Please select type of work');
        $('#addEmpTOW').focus();
        return false;
    } else {
       
    }
}