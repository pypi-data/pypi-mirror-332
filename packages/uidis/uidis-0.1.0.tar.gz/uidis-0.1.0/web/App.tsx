import { render } from "solid-js/web"
import { Navigation } from "./components/Scopes"
import { handleBackgroundImageDrop } from "./core/theme"

const App = () => {
    const onDrop = (e: DragEvent) => {
        if (e.dataTransfer?.files?.length === 1) {
            return handleBackgroundImageDrop(e)
        }
        let content = document.getElementById("content")
        if (content === null) return
        e.preventDefault()
        console.log(e.dataTransfer?.types)
        let card = document.createElement("div")
        card.classList.add("card")
        card.innerHTML = `<h1>${e.dataTransfer?.getData(
            "label"
        )}</h1><h2>${e.dataTransfer?.getData("link")}</h2><h4>Loading...</h4>`
        card.style.position = "absolute"
        card.style.top = `${e.clientY}px`
        card.style.left = `${e.clientX}px`
        content.append(card)
        content.classList.remove("backoff")
        return
    }
    return (
        <>
            <div
                id="content"
                on:drop={onDrop}
                on:dragover={e => e.preventDefault()}
            ></div>
            <Navigation />
        </>
    )
}

render(() => <App />, document.body)
