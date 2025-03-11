import { getVersion, VersionType } from "./server"

var isCacheVersionValidated: boolean = false
var cacheValidationPromise: Promise<void> | null = null

const isVersionZero = (v: VersionType) => v[0] === 0 && v[1] === 0 && v[2] === 0

const areVersionsEqual = (v1: VersionType, v2: VersionType) =>
    v1[0] === v2[0] && v1[1] === v2[1] && v1[2] === v2[2]

export async function validateCache(): Promise<void> {
    if (isCacheVersionValidated) return
    if (cacheValidationPromise !== null) {
        return cacheValidationPromise
    }

    cacheValidationPromise = (async () => {
        const currentVersion = await getVersion()
        const lastKnownVersionString = localStorage.getItem(".ui/version")
        const lastKnownVersion: VersionType = lastKnownVersionString
            ? JSON.parse(lastKnownVersionString)
            : [0, 0, 0]

        if (
            !areVersionsEqual(lastKnownVersion, currentVersion) ||
            isVersionZero(lastKnownVersion)
        ) {
            localStorage.clear()
            localStorage.setItem(".ui/version", JSON.stringify(currentVersion))
        }
        isCacheVersionValidated = true
    })()

    try {
        await cacheValidationPromise
    } catch (error) {
        console.error("Error validating cache:", error)
    }
}
