var updateBtns = document.getElementsByClassName('update-cart')
var currentLocation = window.location;


for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('productId:', productId, 'action:', action)

        console.log('User:', user)
            if (user == "AnonymousUser"){
                  modal.style.display = "block";}
            else
            {

                console.log('Logged in and sending data')
                updateUserOrder(productId,action)
            }
    })
}


function updateUserOrder(producId,action){
    var url ='update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
            body:JSON.stringify({'productId': producId,'action':action})
        })

    .then((response) => {
        return response.json();

    })

    .then((data) => {
        console.log('data', data);


    })
    .then((update)=> {
        console.log(currentLocation.pathname)
        if (currentLocation.pathname == '/cart/'){
            $(".swup").load("/fake_cart");
        }
        //stop()
    })
}
