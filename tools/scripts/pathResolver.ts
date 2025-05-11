enum UserDirectory {
    Work = 'wknowles',
    Personal = 'willknowles',
}

enum AiPath {
    Work = `/Users/${UserDirectory.Work}/Develop/ai/wfkAi`,
    Personal = `/Users/${UserDirectory.Personal}/.wfkAi`,
}

export interface PromptInputs {
    userDir: string;
    rootDir?: string;
    subDir?: string;
}

export interface PromptOutputs {
    absolutePath: string;
}

export function pathResolver(userDir: string) {
    switch (userDir) {
        case UserDirectory.Work:
            return AiPath.Work;
        case UserDirectory.Personal:
            return AiPath.Personal;
        default:
            throw new Error(`BadRequest - Directory Not Found: ${userDir}`);
    }
}