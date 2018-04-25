import '../css/notification.css';
import Notification from '../js/notification';
import Selection from '../js/selection';
import '../tagAdder/jquery.tagsinput';
import '../tagAdder/jquery.tagsinput.css';

const selection = new Selection();
selection.listenMouseUp();

const notification = new Notification();
notification.listen(selection);
