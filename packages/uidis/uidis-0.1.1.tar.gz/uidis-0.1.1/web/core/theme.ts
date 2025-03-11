import materialDynamicColors from "material-dynamic-colors"

export function getBackgroundImage(): Blob | null {
    const b64 = sessionStorage.getItem("background")
    return b64 ? new Blob([atob(b64)], { type: "image/png" }) : null
}

export function applyBackgroundImage(): void {
    const b64 = sessionStorage.getItem("background")
    if (b64) {
        const contentElement = document.querySelector("#content") as HTMLElement
        if (contentElement) {
            contentElement.style.backgroundImage = `url(data:image/jpeg;base64,${b64})`
        }
    }
}

export async function applyTheme() {
    const rootElement = document.querySelector(":root") as HTMLElement
    const image = sessionStorage.getItem("background")
    const source = image ? `data:image/jpeg;base64,${image}` : "#ffd667"
    const themes = await materialDynamicColors(source)
    console.log(themes)

    Object.entries(themes.dark).forEach(([camelName, color]) =>
        rootElement.style.setProperty(
            `--md-sys-color-${camelName
                .replace(/([a-z])([A-Z])/g, "$1-$2")
                .toLowerCase()}`,
            color as string
        )
    )
}

export function handleBackgroundImageDrop(event: DragEvent): Promise<void> {
    return new Promise((resolve, reject) => {
        event.preventDefault()
        event.stopPropagation()

        // Get the dropped file (taking only the first image)
        const files = event.dataTransfer?.files
        if (!files || files.length === 0) {
            reject(new Error("No files were dropped"))
            return
        }

        const file = files[0]

        if (!file.type.startsWith("image/")) {
            reject(new Error("Dropped file is not an image"))
            return
        }

        const reader = new FileReader()

        reader.onload = () => {
            try {
                // Create an image element to get dimensions
                const img = new Image()
                img.onload = () => {
                    // Calculate target size (150% of screen)
                    const targetWidth = Math.round(window.innerWidth * 1.5)
                    const targetHeight = Math.round(window.innerHeight * 1.5)

                    // Create canvas for resizing
                    const canvas = document.createElement("canvas")
                    const ctx = canvas.getContext("2d")

                    if (!ctx) {
                        reject(new Error("Could not create canvas context"))
                        return
                    }

                    // Set canvas size to our target
                    canvas.width = targetWidth
                    canvas.height = targetHeight

                    // Calculate dimensions to maintain aspect ratio while covering the target
                    const imgRatio = img.width / img.height
                    const targetRatio = targetWidth / targetHeight

                    let sourceX = 0
                    let sourceY = 0
                    let sourceWidth = img.width
                    let sourceHeight = img.height

                    if (imgRatio > targetRatio) {
                        // Image is wider than target area - crop the sides
                        sourceWidth = Math.round(img.height * targetRatio)
                        sourceX = Math.round((img.width - sourceWidth) / 2)
                    } else {
                        // Image is taller than target area - crop the top/bottom
                        sourceHeight = Math.round(img.width / targetRatio)
                        sourceY = Math.round((img.height - sourceHeight) / 2)
                    }

                    // Draw image with cropping to fill the entire canvas
                    ctx.drawImage(
                        img,
                        sourceX,
                        sourceY,
                        sourceWidth,
                        sourceHeight, // Source rectangle
                        0,
                        0,
                        targetWidth,
                        targetHeight // Destination rectangle
                    )

                    // Get base64 representation
                    const resizedBase64 = canvas
                        .toDataURL("image/jpeg", 0.85)
                        .split(",")[1]

                    // Store in sessionStorage
                    sessionStorage.setItem("background", resizedBase64)

                    // Apply the background image to #content
                    applyBackgroundImage()
                    applyTheme().then(() => resolve())
                }

                img.onerror = () => {
                    reject(new Error("Failed to load the image for resizing"))
                }

                // Set the image source to the reader result
                img.src = reader.result as string
            } catch (error) {
                reject(error)
            }
        }

        reader.onerror = () => {
            reject(new Error("Failed to read the image file"))
        }

        reader.readAsDataURL(file)
    })
}
