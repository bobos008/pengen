   // 鼠标经过全部分类展示下拉列表
  $(".allList").hover(function(){
    $(".list-jump").slideDown()

  })
//   $(".inventory-box").mouseout(function(){
//   $(".list-jump").stop().slideUp()
//   })
$(".navlist li a").mouseover(function () {
  $(this).addClass("active").parent().siblings().find("a").removeClass("active")

})

//   banner轮播
   var swiper = new Swiper('.swiper-container1', {
      pagination: {
        el: '.swiper-pagination',
      },
    });

         // 点击tab列表切换相关内容
  $(".list-jump li").mouseover(function(){
     var i = $(this).index();//下标第一种写法
            //var i = $('tit').index(this);//下标第二种写法
            // $(".personal").show()
            $(this).find(".personal").show().parent().siblings(".list-jump li").find(".personal").hide()
  });
   $(".inventory-box").mouseleave(function(){
         $(this).find(".personal").hide()
          $(".list-jump").slideUp()

  });    
  $(".tag-block").on("click","li",function(event){
    var target = $(event.target);
    $(this).addClass("active").siblings().removeClass("active")
    var i=$(this).index()
    $(".contentBox").find(".tagcontent").eq(i).addClass("show").siblings().removeClass("show")
  })