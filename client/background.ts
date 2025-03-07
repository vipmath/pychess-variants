import { h, VNode } from 'snabbdom';

import { _ } from './i18n';
import { StringSettings } from './settings';
import { radioList } from './view';

function backgrounds() {
    return {
        light: _("Light"),
        dark: _("Dark"),
    }
}

class BackgroundSettings extends StringSettings {

    constructor() {
        super('theme', 'dark');
    }

    update(): void {
        document.documentElement.setAttribute('data-theme', this.value);
    }

    view(): VNode {
        return h('div#settings-background', radioList(this, 'background', backgrounds(), (_, key) => this.value = key));
    }

}

export const backgroundSettings = new BackgroundSettings();
