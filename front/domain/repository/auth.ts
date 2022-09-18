import { AuthModel } from "../model/auth"

export interface AuthRepository {
    login(email: string, password: string): Promise<AuthModel>
}
