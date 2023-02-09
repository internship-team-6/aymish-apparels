const searchProductListFunction = function () {
  const queryString = location.search;
  const urlParams = new URLSearchParams(queryString);
  const limit = 15;
  const page = parseInt(urlParams.get("page"));
  const offset = (page - 1) * limit;
  const sort = urlParams.get("sort");
  let q = urlParams.get("q");
  q = q == "" ? "*" : q;
  document.getElementById(
    "path"
  ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${
    q[0].toUpperCase() + q.slice(1)
  }`;
  document.getElementById("search-for").innerHTML = q;
  document.getElementById("product-query").innerHTML = q == "*" ? "all" : q;
  fetch(
    "http://localhost:5000/search?" + new URLSearchParams({ q: q, sort: sort }),
    {
      method: "GET",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
        Accept: "application/json",
        "Content-Type": "application/json;charset=utf-8",
      },
    }
  )
    .then((response) => response.json())
    .then((data) => {
      const products_arr = data;
      console.log(products_arr);
      let prod_list_div = document.getElementById("product-list-div");
      for (
        let counter = offset;
        counter < Math.min(offset + limit, products_arr.length);
        counter++
      ) {
        let title = products_arr[counter]["title"];
        let image = products_arr[counter]["image"];
        let price = products_arr[counter]["price"];
        let id = products_arr[counter]["id"];
        prod_list_div.innerHTML += `
          <div class="product-container" id="product-list-div" onclick = "window.open('Product.html?uniqueId=${id}','_blank');">
            <div class="product-card">
              <div class="product-image">
                <img src="${image}" class="product-thumb product-border" alt="" />
              </div>
              <div class="product-info">
                <p class="product-title">${title}</p>
                <span class="price">$${price}</span>
              </div>
            </div>
          </div>
        `;
      }
      const pages =
        Math.floor(products_arr.length / 15) + (products_arr.length % 15 && 1);

      let paginationId = document.getElementById("pagination");
      if (page !== 1) {
        let pageSearchParams = new URLSearchParams({
          q: q,
          sort: sort,
          page: page - 1,
        });
        paginationId.innerHTML += `<a href="./search-product-list.html?${pageSearchParams}">◀◀</a>`;
      }
      for (let temp_page = 1; temp_page <= pages; temp_page++) {
        let pageSearchParams = new URLSearchParams({
          q: q,
          sort: sort,
          page: temp_page,
        });
        if (temp_page === page) {
          console.log(temp_page);
          paginationId.innerHTML += `<a class = "active" href="./search-product-list.html?${pageSearchParams}">${temp_page}</a>`;
        } else {
          paginationId.innerHTML += `<a href="./search-product-list.html?${pageSearchParams}">${temp_page}</a>`;
        }
      }
      if (page !== pages) {
        let pageSearchParams = new URLSearchParams({
          q: q,
          sort: sort,
          page: page + 1,
        });
        paginationId.innerHTML += `<a href="./search-product-list.html?${pageSearchParams}">▶▶</a>`;
      }
    });
};

window.onload = searchProductListFunction();
