let knapper = document.querySelectorAll('.add-cart');
console.log(knapper);

//Products
let products = [
    {
        name: 'bilde1',
        tag: 'tag1',
        price: 1000,
        inCart: 0
    },
    {
        name: 'bilde2',
        tag: 'tag2',
        price: 1500,
        inCart: 0
    },

    {
        name: 'bilde3',
        tag: 'tag3',
        price: 300,
        inCart: 0
    },

    {
        name: 'bilde4',
        tag: 'tag4',
        price: 440,
        inCart: 0
    },
]; 

//Når du klikker på en av knappene, adder func
for(let i = 0; i < knapper.length; i++){
    
    knapper[i].addEventListener('click', () => {
        cartNumbers(products[i]);
        totalKostnad(products[i]);
    })
}

//Holder localstorage, når man oppdaterer nettsiden
function oppdaterHandlekurv(){
    let countProducts = localStorage.getItem('cartNumbers');
    
    if(countProducts){
        document.querySelector('.cart span').textContent = countProducts;
    }
}

//Teller for local storage og antall produkter som vises i ikonet
function cartNumbers(product){
    let countProducts = localStorage.getItem('cartNumbers');
    countProducts = parseInt(countProducts);


    if(countProducts){
        localStorage.setItem('cartNumbers', countProducts + 1);
        document.querySelector('.cart span').textContent = countProducts + 1;
    }else{
        localStorage.setItem('cartNumbers',1);
        document.querySelector('.cart span').textContent = 1;
    }
    setItems(product);
}




//Finn ut hvilke produkt som blir klikket på -> referer med produkt i hele linjen, oppdater ant produkter
function setItems(product){
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);
    console.log(cartItems);
    // cartItems = JSON.parse(cartItems);
    // console.log("My cartitems are:", cartItems);

    //Sjekker om den eksisterer ikke, om den eksisterer -> teller opp nåværernde produkt
    if(cartItems != null){

        if(cartItems[product.tag] == undefined){
            cartItems = {
                ...cartItems, //Resterende produkter igjen (ikke blitt trukket på enda)
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart += 1;
    }else{
        product.inCart = 1;
        cartItems = {
            [product.tag] : product
        }
    }

    localStorage.setItem("productsInCart", JSON.stringify(cartItems));

}

function totalKostnad(product){
    let cartCost = localStorage.getItem('totalKostnad');
    

    
    if(cartCost != null){
        cartCost = parseInt(cartCost); //Hvorfor må vi konvertere her? og ikke før?
        localStorage.setItem('totalKostnad', cartCost + product.price);
    }else{
        localStorage.setItem('totalKostnad', product.price);
    }
}

function visHandlekurv(){
    const ut="";
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    let productContainer = document.querySelector(".products");
    let cartCost = localStorage.getItem('totalKostnad');
    if(cartItems && productContainer){
        productContainer.innerHTML = "";
        Object.values(cartItems).map(item => {
           //Skriv ut tabell

            productContainer.innerHTML += `
                <tr class="product">
                    <td>
                        <ion-icon name="basket"></ion-icon>
                        <img src="./static/card1.jpg"  style="width:40px; height=40px;">
                        <span>${item.name} </span>
                    </td>
                    <td class="price">${item.price},00 kr</td>
                    <td class="quantity">${item.inCart}</td>
                    <td class="total">${item.inCart * item.price} kr </td>
                    
                </tr> 
                `
            });
            productContainer.innerHTML += `
                <div>
                <h4 class="basketTotalTitle">
                    Total:
                </h4>
                <h4 class="basketTotal">
                    ${cartCost},00 kr
                </h4>
                </div>
                `
       

    }
}

oppdaterHandlekurv();
visHandlekurv();
