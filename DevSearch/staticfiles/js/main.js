let searchForm=document.getElementById('searchForm')
let page_links=document.getElementsByClassName('page-link')


    if (searchForm){
        for (let i=0; i<page_links.length;i++){
            page_links[i].addEventListener('click',function (e){
                e.preventDefault()

                let page=this.dataset.page
                console.log(page)

                searchForm.innerHTML+=`<input value=${page} name="page" hidden/>`

                searchForm.submit()


            })
        }

    }



    // const tags=document.querySelectorAll(".project--tag")
    // for (let i=0;i<tags.length;i++){
    //     tags[i].addEventListener('click',(e)=>{
    //         const tagId=e.target.dataset.tag
    //         const projectId=e.target.dataset.project
    //         console.log("Tag Id: ",tagId)
    //         console.log("Project Id: ",projectId)
    //         fetch("http://127.0.0.1:8000/api/remove/tag/",{
    //             method:"DELETE",
    //             headers: {
    //                 'Content-Type': 'application/json',
    //             },
    //             body: JSON.stringify({
    //                 'tagId':tagId,
    //                 'projectId':projectId
    //             })
    //         })
    //             .then(response=>response.json())
    //             .then(data=>{
    //                 e.target.remove()
    //             })
    //     })
    // }