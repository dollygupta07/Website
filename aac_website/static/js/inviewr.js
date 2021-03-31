function inviewExample() {
     var $example = $('#inview-example');
     var inview;

     if ($example.length) {
       inview = new Waypoint.Inview({
         element: $('#inview-example')[0],
         entered: function(direction) {
           $('.timer').each(function () {
               var $this = $(this);
               var val = $(this).data('count');
               jQuery({ Counter: 0 }).animate({ Counter: val }, {
                 duration: 1000,
                 easing: 'swing',
                 step: function () {
                   $this.text(Math.ceil(this.Counter));
                 }
               });
             });
         }
       })
     }
 }
$(window).on('load', function() {
  inviewExample();
})
