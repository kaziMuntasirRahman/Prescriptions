var ShoppingCart = (function($) {
  "use strict";
  
  // Cahce necesarry DOM Elements
  var patientsEl = document.querySelector(".patients"),
      cartEl =     document.querySelector(".shopping-cart-list"),
      patientQuantityEl = document.querySelector(".patient-quantity"),
      emptyCartEl = document.querySelector(".empty-cart-btn"),
      cartCheckoutEl = document.querySelector(".cart-checkout"),
      totalPriceEl = document.querySelector(".total-price");
  
  // Fake JSON data array here should be API call
  var patients = [
    {
      id: 0,
      name: "John Cena",
      description: "Male Patient with age of 35. Athlete body.",
      imageUrl: "./img2/patient1.png",
      // price: 1
    },
    {
      id: 1,
      name: "Ayesha Begum",
      description: "Female Patient.",
      imageUrl: "./img2/patient2.png",
      // price: 1999,
    },
    {
      id: 2,
      name: "Abu Huraiyah",
      description: "Kid male Patient.",
      imageUrl: "./img2/patient3.jpg",
      // price: 1499
    },
    {
      id: 3,
      name: "Fatima Akhtar",
      description: "Female Patient",
      imageUrl: "./img2/patient4.jpg",
      // price: 999
    },
    {
      id: 4,
      name: "Khadija Begum",
      description: "Female Old Patient",
      imageUrl: "./img2/patient5.png",
      // price: 599
    },
    {
      id: 5,
      name: "Abdur Rahman",
      description: "Male Old Patient",
      imageUrl: "./img2/patient6.png",
      // price: 499
    }
  ],
      patientsInCart = [];
  
  // Pretty much self explanatory function. NOTE: Here I have used template strings (ES6 Feature)
  var generatepatientList = function() {
    patients.forEach(function(item) {
      var patientEl = document.createElement("div");
      patientEl.className = "patient";
      patientEl.innerHTML = `<div class="patient-image">
                                <img src="${item.imageUrl}" alt="${item.name}">
                             </div>
                             <div class="patient-name"><span>patient:</span> ${item.name}</div>
                             <div class="patient-description"><span>Description:</span> ${item.description}</div>
                             <div class="patient-price"><span>Price:</span> ${item.price} $</div>
                             <div class="patient-add-to-cart">
                               <a href="#0" class="button see-more">More Details</a>
                               <a href="#0" class="button add-to-cart" data-id=${item.id}>Mark as Seen</a>
                             </div>
                          </div>
`;
                             
patientsEl.appendChild(patientEl);
    });
  }
  
  // Like one before and I have also used ES6 template strings
  var generateCartList = function() {
    
    cartEl.innerHTML = "";
    
    patientsInCart.forEach(function(item) {
      var li = document.createElement("li");
      li.innerHTML = `${item.quantity} ${item.patient.name} - $${item.patient.price * item.quantity}`;
      cartEl.appendChild(li);
    });
    
    patientQuantityEl.innerHTML = patientsInCart.length;
    
    generateCartButtons()
  }
  
  
  // Function that generates Empty Cart and Checkout buttons based on condition that checks if patientsInCart array is empty
  var generateCartButtons = function() {
    if(patientsInCart.length > 0) {
      emptyCartEl.style.display = "block";
      cartCheckoutEl.style.display = "block"
      totalPriceEl.innerHTML = "$ " + calculateTotalPrice();
    } else {
      emptyCartEl.style.display = "none";
      cartCheckoutEl.style.display = "none";
    }
  }
  
  // Setting up listeners for click event on all patients and Empty Cart button as well
  var setupListeners = function() {
    patientsEl.addEventListener("click", function(event) {
      var el = event.target;
      if(el.classList.contains("add-to-cart")) {
       var elId = el.dataset.id;
       addToCart(elId);
      }
    });
    
    emptyCartEl.addEventListener("click", function(event) {
      if(confirm("Are you sure?")) {
        patientsInCart = [];
      }
      generateCartList();
    });
  }
  
  // Adds new items or updates existing one in patientsInCart array
  var addToCart = function(id) {
    var obj = patients[id];
    if(patientsInCart.length === 0 || patientFound(obj.id) === undefined) {
      patientsInCart.push({patient: obj, quantity: 1});
    } else {
      patientsInCart.forEach(function(item) {
        if(item.patient.id === obj.id) {
          item.quantity++;
        }
      });
    }
    generateCartList();
  }
  
  
  // This function checks if project is already in patientsInCart array
  var patientFound = function(patientId) {
    return patientsInCart.find(function(item) {
      return item.patient.id === patientId;
    });
  }

  var calculateTotalPrice = function() {
    return patientsInCart.reduce(function(total, item) {
      return total + (item.patient.price *  item.quantity);
    }, 0);
  }
  
  // This functon starts the whole application
  var init = function() {
    generatepatientList();
    setupListeners();
  }
  
  // Exposes just init function to public, everything else is private
  return {
    init: init
  };
  
  // I have included jQuery although I haven't used it
})(jQuery);

ShoppingCart.init();