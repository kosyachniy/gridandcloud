import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainComponent} from './main/main.component';
import { AuthGuard } from './auth.guard';
import {StartComponent} from "./start/start.component";

const routes: Routes = [
    {path: '', component:  MainComponent},
    {path: 'start', component:  StartComponent, canActivate: [AuthGuard] },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
}
