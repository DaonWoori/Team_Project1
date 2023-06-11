// {/* <script language = "javascript"> */}

// function ShowSliderValue(sVal)
// {
//     var obValueView = document.getElementById("slider_value_view");
//     obValueView.innerHTML = sVal
// }

// var RangeSlider = function(){
//     var range = $('.slider_range');
    
//     range.on('input', function(){		
//         ShowSliderValue(this.value);
//     });
// };

// RangeSlider();

var rangeSlider = function(){
    var slider = $('.range-slider'),
        range = $('.range-slider__range'),
        value = $('.range-slider__value');
      
    slider.each(function(){
  
      value.each(function(){
        var value = $(this).prev().attr('value');
        $(this).html(value);
      });
  
      range.on('input', function(){
        $(this).next(value).html(this.value);
      });
    });
  };
  
rangeSlider();