import axios, { AxiosInstance } from "axios";
import { AuthModel } from "../domain/model/auth";
import { AuthRepository } from "../domain/repository/auth";


export class AuthInfrastructure implements AuthRepository {
    private _axios: AxiosInstance

    constructor() {
        this._axios = axios.create({
            baseURL: 'http://localhost:8000',
            responseType: 'json',
            headers: {
                'Content-Type': 'application/json',
            }
        })
    }

    async login(email: string, password: string): Promise<AuthModel> {
        try {
            const result = await this._axios.post<AuthModel>(
                '/api/auth/jwt/create',
                {
                    'email': email,
                    'password': password
                }
            )
            console.log(result)
            return result.data
        } catch (e) {
            console.log('Error!!!!!')
            console.error(e)
            throw e
        }
    }

}