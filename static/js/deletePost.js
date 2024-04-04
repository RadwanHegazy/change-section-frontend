var boxes = document.querySelectorAll('.content .box');
var deletOerlay = document.querySelector('.delete-overlay');
var PostId = deletOerlay.querySelector('input[name=post_id]');
var CancelOverlay = document.getElementById('cancel');

boxes.forEach(box=>{

    var deleteBtn = box.querySelector('.icons a.del');
    deleteBtn.addEventListener('click',()=>{
        PostId.value = box.dataset.postid;
        deletOerlay.classList.add('view');
    })

})

CancelOverlay.addEventListener('click',function(){
    deletOerlay.classList.remove('view');
})
