export enum CaseTransformer {
    PascalCase,
    CamelCase,
    KebabCase,
    SnakeCase,
}

function toPascalCase(str: string): string {
    return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join('');
}

function toCamelCase(str: string): string {
    return str.split(' ').map((word, index) => index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1)).join('');
}

function toKebabCase(str: string): string {
    return str.split(' ').map(word => word.toLowerCase()).join('-');
}

function toSnakeCase(str: string): string {
    return str.split(' ').map(word => word.toLowerCase()).join('-');
}

export function caseTransformer(str: string, transformCase: CaseTransformer): string {
    switch (transformCase) {
        case CaseTransformer.PascalCase:
            return toPascalCase(str);
        case CaseTransformer.CamelCase:
            return toCamelCase(str);
        case CaseTransformer.KebabCase:
            return toKebabCase(str);
        case CaseTransformer.SnakeCase:
            return toSnakeCase(str);
        default:
            return str;
    }
}

export type Persona = {
    id: string;
    name: string;
    source: string;
}

export type BuildPanelError = {
    persona: Persona;
    error: string;
    data?: any;
}

export type SMEPanel = {
    panel: Persona[];
    errors: BuildPanelError[];
}


export function isValidPersona(persona: Persona): boolean {
    return true
}

export function buildPanel(...panel: Persona[]): SMEPanel {
    const response: SMEPanel = {
        panel,
        errors: [],
    }

    response.panel = response.panel.reduce( (acc: Persona[], persona: Persona) => {
        if (!isValidPersona(persona)) {
            response.errors.push({
                persona,
                error: "BuildPanelError: Malformed Persona",
            });
            return acc;
        }
        acc.push(persona);
        return acc;
    }, []);

    return response;
}