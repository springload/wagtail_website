import $ from 'jquery';
import 'jquery-ui/ui/widgets/datepicker';
import Popper from 'popper.js';

import 'bootstrap';

(window as any).$ = $;
(window as any).jQuery = $;
(window as any).Popper = Popper;

document.documentElement.classList.remove('no-js');
