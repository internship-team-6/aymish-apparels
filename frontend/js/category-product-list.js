// parameters to connect while using the fetch promise on any given url
var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};

// function to navigate to category-product-list page based on the provided sort order
const categorySelectSort = (sort) => {
  let params = new URLSearchParams(window.location.search);
  let catlevel2Id = params.get("catlevel2Id");
  window.location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel2Id: catlevel2Id,
      sort: sort.value,
      page: 1,
    });
};

window.onload = (() => {
  const queryString = window.location.search;
  
  // get values for parameters
  const urlParams = new URLSearchParams(queryString);
  const page = parseInt(urlParams.get("page"));
  const catlevel2Id = urlParams.get("catlevel2Id");
  const sort = urlParams.get("sort");

  // get no. of pages for the given category 
  fetch(
    "http://localhost:5000/category-pagination?" +
      new URLSearchParams({ catlevel2Id: catlevel2Id }),
    connectionParams
  )
    .then((response) => response.json())
    .then((data) => {
      let pages = parseInt(data);

      // get tree of names for category and its parent categories in bottom-up manner 
      fetch(
        "http://localhost:5000/name-tree?" +
          new URLSearchParams({ catlevel2Id: catlevel2Id }),
        connectionParams
      )
        .then((response) => response.json())
        .then((data) => {
          let categoryPath = data.reduce((x, y) => x + "/" + y);
          document.getElementById(
            "path"
          ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${categoryPath}`;
          document.getElementById("product-query").innerHTML = categoryPath;
          document.getElementById("cat-title").innerHTML = catlevel2Id;
          let catParamsMap = { catlevel2Id: catlevel2Id, page: page };
          if (sort !== null && sort.length !== 0) {
            catParamsMap["sort"] = sort;
          }
          document.title = "Product list for category" + categoryPath;

          // get list of products belonging to the given category
          fetch(
            "http://localhost:5000/category-product-list?" +
              new URLSearchParams(catParamsMap),
            connectionParams
          )
            .then((response) => response.json())
            .then((data) => {
              const productsArr = data;

              // update page with product details
              let prodListDiv = document.getElementById("product-list-div");
              const newInnerHTML = productsArr
                .map(
                  (product) => `
                      <div class="product-container" id="product-list-div" onclick = "window.open('product.html?uniqueId=${product["id"]}','_blank');">
                        <div class="product-card">
                          <div class="product-image">
                            <img src="${product["image"]}" class="product-thumb product-border" alt="" />
                          </div>
                          <div class="product-info">
                            <p class="product-title">${product["title"]}</p>
                            <p class="price">$${product["price"]}</p>
                          </div>
                        </div>
                      </div>
                      `
                )
                .reduce((x, y) => x + y);
              prodListDiv.innerHTML += newInnerHTML;

              // update page with pagination indicators
              let paginationId = document.getElementById("pagination");
              if (page !== 1) {
                paginationId.innerHTML += `<a href="./category-product-list.html?${new URLSearchParams(
                  {
                    ...catParamsMap,
                    page: page - 1,
                  }
                )}">&#10094;</a>`;
                paginationId.innerHTML += `<a href="./category-product-list.html?${new URLSearchParams(
                  { ...catParamsMap, page: 1 }
                )}">1</a>`;
              }
              paginationId.innerHTML += `<a class="active" href="./category-product-list.html?${new URLSearchParams(
                { ...catParamsMap, page: page }
              )}">${page}</a>`;
              if (page !== pages) {
                paginationId.innerHTML += `
              <a href="./category-product-list.html?${new URLSearchParams({
                ...catParamsMap,
                page: pages,
              })}">${pages}</a>`;
                paginationId.innerHTML += `<a href="./category-product-list.html?${new URLSearchParams(
                  {
                    ...catParamsMap,
                    page: page + 1,
                  }
                )}">&#10095;</a>`;
              }
            })
            .catch((err) => {
              window.location.href = "./404.html?";
            });
        })
        .catch((err) => {
          window.location.href = "./404.html?";
        });
    })
    .catch((err) => {
      window.location.href = "./404.html?";
    });
})();
