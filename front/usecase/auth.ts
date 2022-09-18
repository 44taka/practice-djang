import { AuthInfrastructure } from "../infrastructure/auth";


export class AuthUseCase {

    private auth_infrastructure: AuthInfrastructure

    constructor() {
        this.auth_infrastructure = new AuthInfrastructure()
    }

    async login(email: string, password: string) {
        try {
            return await this.auth_infrastructure.login(email, password)
        } catch (e) {
            console.log('Error2!!!!')
            console.error(e.messages)
            throw e
        }
    }
}
