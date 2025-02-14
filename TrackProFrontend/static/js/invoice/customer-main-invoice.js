 
  $(document).ready(function() {

    var colorId = $(".colorId").text()
    console.log("colorId",colorId.split(","))
    var singleArray = colorId.split(",")
    singleArray.pop()
    console.log(singleArray)
    $(singleArray).each(function(o,i){
    subProductTotal(i);
    })
    calculateAmount();
  })

  function subProductTotal(id){

   var quantityTotal = $(".rowQuantity"+id)
   var quantity = 0 
      for (var i = 0; i < quantityTotal.length; i++) {
        quantity += parseFloat(quantityTotal[i].innerHTML);
      }
    $(".subQuantityTotal"+id).html((quantity))

  var totalAmount=$(".colorPrice"+id)
    var total = 0
      for (var i = 0; i < totalAmount.length; i++) {
          total += parseFloat(totalAmount[i].innerHTML);
      }
    $(".subProductTotal"+id).html((total).toFixed(2))

  var discountAmount = $(".discountPrice"+id)
  var distotal = 0
      for (var i = 0; i < discountAmount.length; i++) {
          distotal += parseFloat(discountAmount[i].innerHTML);
      }
    $(".subDiscountTotal"+id).html((distotal).toFixed(2))

  var gstAmount = $(".gstPrice"+id)
  var gstTotal = 0
      for (var i = 0; i < gstAmount.length; i++) {
          gstTotal += parseFloat(gstAmount[i].innerHTML);
      }
    $(".subGstTotal"+id).html((gstTotal).toFixed(2))
    $(".cgstAmt"+id).html((parseFloat(gstTotal)/2).toFixed(2))

    var taxableAmt = parseFloat(total + gstTotal ) - parseFloat(distotal)
    $(".subRowTotal"+id).html(taxableAmt.toFixed(2))

    var quantityTotal = $(".quantityTotal")
    var qty = 0
      for (var i = 0; i < quantityTotal.length; i++) {
        qty += parseFloat(quantityTotal[i].innerHTML);
      }
    $("#quantityTotal").html((qty))
    $("#sumQty").html((qty))

    var productTotal = $(".productTotal")
    var prAmt = 0
      for (var i = 0; i < productTotal.length; i++) {
          prAmt += parseFloat(productTotal[i].innerHTML);
      }
    $("#productTotal").html((prAmt).toFixed(2))
    $("#sumTaxable").html((prAmt).toFixed(2))

    var discTotal = $(".discTotal")
    var discAmt = 0
    for (var i = 0; i < discTotal.length; i++) {
          discAmt += parseFloat(discTotal[i].innerHTML);
      }
    $("#discTotal").html((discAmt).toFixed(2))

    var mainGstTotal = $(".mainGstTotal")
    var mainGstAmt = 0
    for (var i = 0; i < mainGstTotal.length; i++) {
      mainGstAmt += parseFloat(mainGstTotal[i].innerHTML);
      }
    $("#mainGstTotal").html((mainGstAmt).toFixed(2))
    $(".sumIgstTotal").html((mainGstAmt).toFixed(2))
    $(".sumCgstTotal").html((parseFloat(mainGstAmt)/2).toFixed(2))
    var payableAmt = parseFloat(prAmt + mainGstAmt ) - parseFloat(discAmt)
    $("#billTotal").html(payableAmt.toFixed(2))
    $("#sumBillTotal").html(payableAmt.toFixed(2))
   
  
    var totalBill = $('#netBillTotal').html();
    
    
    var totalinwords = price_in_words(parseFloat(totalBill));
    $("#totalInWord").html(totalinwords)
  }

  function calculateAmount(){
    var sumBillTotal = $("#sumBillTotal").text()
    var mainBillDiscount = parseFloat($("#mainBillDiscount").text())
    var mainFreight = parseFloat($("#mainFreight").text())
    var payableAmt = (parseFloat(sumBillTotal) + parseFloat(mainFreight)) - parseFloat(mainBillDiscount)
    $(".sumBillTotal").html(payableAmt.toFixed(0))
    var totalBill = $('#netBillTotal').html();
    var totalinwords = price_in_words(parseFloat(totalBill));
    $("#totalInWord").html(totalinwords)
    var creditAmount = $("#creditAmount").text()
    var cashPaid = $("#cashPaid").text()
    
    if (creditAmount > 0){
      if (parseFloat(cashPaid) != 0){
        var balanceAmount = (parseFloat(creditAmount) - parseFloat(totalBill)) - parseFloat(cashPaid)
        if (balanceAmount < 0){
          $("#balanceAmount").text(0);
        }else{
          $("#balanceAmount").text(balanceAmount.toFixed(2));
        }
      }else {
        var balanceAmount = (parseFloat(totalBill) - parseFloat(creditAmount));
        $("#balanceAmount").text(balanceAmount.toFixed(2));
      }
    }
  
  
  }
  
  function price_in_words(price) {
        var sglDigit = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"],
          dblDigit = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
          tensPlace = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"],
          handle_tens = function(dgt, prevDgt) {
            return 0 == dgt ? "" : " " + (1 == dgt ? dblDigit[prevDgt] : tensPlace[dgt])
          },
          handle_utlc = function(dgt, nxtDgt, denom) {
            return (0 != dgt && 1 != nxtDgt ? " " + sglDigit[dgt] : "") + (0 != nxtDgt || dgt > 0 ? " " + denom : "")
          };
      
        var str = "",
          digitIdx = 0,
          digit = 0,
          nxtDigit = 0,
          words = [];
        if (price += "", isNaN(parseInt(price))) str = "";
        else if (parseInt(price) > 0 && price.length <= 10) {
          for (digitIdx = price.length - 1; digitIdx >= 0; digitIdx--) switch (digit = price[digitIdx] - 0, nxtDigit = digitIdx > 0 ? price[digitIdx - 1] - 0 : 0, price.length - digitIdx - 1) {
            case 0:
              words.push(handle_utlc(digit, nxtDigit, ""));
              break;
            case 1:
              words.push(handle_tens(digit, price[digitIdx + 1]));
              break;
            case 2:
              words.push(0 != digit ? " " + sglDigit[digit] + " Hundred" + (0 != price[digitIdx + 1] && 0 != price[digitIdx + 2] ? " and" : "") : "");
              break;
            case 3:
              words.push(handle_utlc(digit, nxtDigit, "Thousand"));
              break;
            case 4:
              words.push(handle_tens(digit, price[digitIdx + 1]));
              break;
            case 5:
              words.push(handle_utlc(digit, nxtDigit, "Lakh"));
              break;
            case 6:
              words.push(handle_tens(digit, price[digitIdx + 1]));
              break;
            case 7:
              words.push(handle_utlc(digit, nxtDigit, "Crore"));
              break;
            case 8:
              words.push(handle_tens(digit, price[digitIdx + 1]));
              break;
            case 9:
              words.push(0 != digit ? " " + sglDigit[digit] + " Hundred" + (0 != price[digitIdx + 1] || 0 != price[digitIdx + 2] ? " and" : " Crore") : "")
          }
          str = words.reverse().join("")
        } else str = "";
        return str
      
      }

      $('#download').click(function(){
        $('#download').hide();
        CreatePDFfromHTML();
        $('#download').show();
    })

    function CreatePDFfromHTML() {
        var HTML_Width = $("#content").width();
        var HTML_Height = $("#content").height();
        var top_left_margin = 15;
        var PDF_Width = HTML_Width + (top_left_margin * 2);
        var PDF_Height = (PDF_Width * 1.2) + (top_left_margin * 2);
        var canvas_image_width = HTML_Width;
        var canvas_image_height = HTML_Height;
    
        var totalPDFPages = Math.ceil(HTML_Height / PDF_Height) - 1;
    
        html2canvas($("#content")[0]).then(function (canvas) {
           
            var imgData = canvas.toDataURL("image/jpeg", 1.0);
            var pdf = new jsPDF('p', 'pt', [PDF_Width, PDF_Height]);
            pdf.addImage(imgData, 'JPG', top_left_margin, top_left_margin, canvas_image_width, canvas_image_height);
            for (var i = 1; i <= totalPDFPages; i++) { 
                pdf.addPage(PDF_Width, PDF_Height);
                pdf.addImage(imgData, 'JPG', top_left_margin, -(PDF_Height*i)+(top_left_margin*4),canvas_image_width,canvas_image_height);
              
            }
            
            pdf.save("Invoice.pdf");
           
           
        });
        
    }

