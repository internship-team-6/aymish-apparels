window.onload = myFunction = function () {
  let q = localStorage.getItem("query");
  if (q != "") {
    fetch("http://localhost:5000/search?" + new URLSearchParams({ q: q }), {
      method: "GET",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
        Accept: "application/json",
        "Content-Type": "application/json;charset=utf-8",
      },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        //window.location.href = "http://localhost:5500/frontend/product-list.html?";
        const products_arr = data["products"];
        let prod_list_div = document.getElementById("product-list-div");
        for (let i = 0; i < products_arr.length; i++) {
          let title = products_arr[i]["title"];
          let img = products_arr[i]["img"];
          let price = products_arr[i]["price"];
          let id = products_arr[i]["id"];
          prod_list_div.innerHTML += `<div class="product-container" id="product-list-div" onclick = "window.open('Product.html?uid=${id}','_blank');">
          <div class="product-card">
              <div class="product-image">
                <img src="${img}" class="product-thumb" alt="" />
              </div>
              <div class="product-info">
                <p class="product-title">${title}</p>
                <span class="price">$${price}</span>
              </div>
            </div>
            </div>`;
        }
      });
  }
  // window.location.href = "http://localhost:5500/frontend/product-list.html?";
};
