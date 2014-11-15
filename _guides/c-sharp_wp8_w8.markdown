---
layout: post
title: "C-Sharp, WP8, W8"
date: 2014-03-16 20:48:22 +0100
comments: true
categories:
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

#C-Sharp

## Delegates and Events

ref: http://csharpindepth.com/Articles/Chapter2/Events.aspx
Delegates and Events are easy to confuse. C# doesn't help matters by allowing you to declare field-like events (sintassi simile a come dichiari un membro di classe, ex:Prime31 ) which are automatically backed by a delegate variable of the same name.

A delegate type as being a bit like an interface with a single method. It specifies the signature of a method, and when you have a delegate instance, you can make a call to it as if it were a method with the same signature. If you come from c++ it's similar to a function pointer.

Delegates hold a reference to a method, and (for instance methods) a reference to the target object the method should be called on.

Why delegate exists if we have Interface?
Delegates are interface with syntactic sugar, it allow you to quickly declare an interface with only one method.

Calling delegate instances
The C# syntax is just a short-hand for calling the Invoke method provided by each delegate type

!!!! First things first: events aren't delegate instances. Let's try that again.

Events are pairs of methods, appropriately decorated in IL to tie them together and let languages know that the methods represent events.

# W8 and WP8 threads, dispatcher, etc

## Understanding Windows Store App and Windows Phone 8 Threads

When an app is executed there are multiple threads instantiated:

* `User Interface (UI) thread`: Indicates screen updates and touch inputs. You should try to keep the UI thread to less than 50% of CPU usage.
* `Application Threads`: A thread that is not the UI thread. This could be composition thread or background threads.
* `System Threads`: Thread that are not for the app. A large system thread percentage indicates that the system is busy with other background tasks and is affecting app performance.

What they do:

* `UI Thread`: Windows Store apps using C++, C#, or Visual Basic are event-driven and all UI components share the same thread.
Event-driven means that your code executes when an event occurs. After your app completes the work that is in response to an event, it sits idle, waiting for the next event to occur. The framework code for UI (running layout, processing input, firing events, and so on) and an app’s code for UI all are executed on the same thread. Only one piece of code can execute at a time, so if your app code takes too long to run, the framework can’t run layout or notify an app of other events that fired. In other words, the responsiveness of your app is directly related to the availability of the UI thread to process work. The less work you are doing on the UI thread, the more responsive your program will be to user input.
* `Composition Thread`: The composition thread handles some work that the UI thread would normally handle, and therefore improves performance of Windows Phone apps. The composition thread combines graphics textures and passes them to the GPU for drawing. Also, on Windows Phone storyboard-driven animations that run on the composition thread are automatically cached and handled by the GPU on the device in a process called auto-caching.
The composition thread handles simple animations associated with the RenderTransform and Projection properties
* `Other Thread`: they could belong to a Thread Pool or they can be
    generic.

Reference Windows Store:
http://msdn.microsoft.com/en-us/library/windows/apps/hh994635.aspx

Reference WP8:
http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff967560%28v=vs.105%29.aspx#BKMK_Understandingthreads


## Safe Intra Thread Comunication between the UI and the other threads
When code that updates the UI executes from a thread other than the UI thread, an invalid cross-thread access exception occurs.

The UI thread has a Dispatcher that can be used to safely execute code that update the UI from the UI thread. To get the Dispatcher of the UI thread use the Deployment.current static method:
`Deployment.Current.Dispatcher.BeginInvoke( ()=> {...}`

Its safe to call the code above from another thread.

Marco Ventilii: mi viene in mente che se passiamo riferimenti a strutture non thread safe nella callback e poi quelle strutture vengono modificate/lette sia nel thread UI che in quello generico che chiama il dispatcher, potrebbe succedere comunque un casino....

ref: http://stackoverflow.com/questions/4679324/what-is-the-use-of-deployment-current-dispatcher-begininvoke
ref: Deployment Class
Getting the UI Thread from c++: http://robwirving.com/2013/07/17/guide-to-getting-to-the-ui-thread-for-any-type-of-windows-phone-8-app/

When you are not sure if in which thread you code is running you can use this tips:

* Most of the UI components derive from a DependencyObject:
    http://msdn.microsoft.com/en-us/library/windowsphone/develop/system.windows.dependencyobject%28v=vs.105%29.aspx#inheritanceContinued
    DependencyObject has an helper to check if we accessing the object
    from access a NON UI thread : `DependencyObject.CheckAccess Method`
http://msdn.microsoft.com/en-us/library/windowsphone/develop/system.windows.dependencyobject.checkaccess(v=vs.105).aspx
*  Use Thread.CurrentThread
http://msdn.microsoft.com/en-us/library/system.threading.thread.currentthread(v=vs.80).aspx
Example: http://stackoverflow.com/questions/1149402/how-to-detect-if-were-on-a-ui-thread

NB: Code located in App.xaml.cs, MainPage.xaml.cs is always running on UI thread.
MISC example with Unity3D and WP8: https://github.com/windowsgamessamples/UnityPorting

## Example Unity3D
Most of the unity 3D plugins require to run code on the UI thread but the engine itself is processing its script on a different thread.
Marco Ventilii aggiungi un esempio usando CurrentThread
From the Unity3D thread we can use Deployment.Current.Dispatcher.BeginInvoke.
But most of the Unity3D classes are not thread safe (ref),  if we need to call something, for example a callback, on a Unity3D object from the UI thread we must use do it in a thread safe way.

Marco Ventiliiqua ci va tutto il discorso delle DLL per accedere al metodo magico da una DLL

Example: http://unitygems.com/threads/



# WP8 Push notifications: client and server implementation

WP8 push notifications are similar to iOS and Android push, see here for a general overview:
http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff402558%28v=vs.105%29.aspx

Notification types are:

* tile
* toast
* raw

Your WP8 app must be configured, the setup is described here:
http://msdn.microsoft.com/en-us/library/windowsphone/develop/hh202940%28v=vs.105%29.aspx

## Production server

Our production cloud server MUST use a certificate to authenticate for no-quota (unthrottled) push notifications.

### TLS Authentication

**ISSUES with WILDCARD CERT, cannot use them, use the placecommander.com
certificate**


http://social.msdn.microsoft.com/Forums/wpapps/en-US/3f518b21-5727-4d43-bfe6-9e3efb41da3c/wildcard-entry-for-push-notification-certificate?forum=wpnotifications
But we can use the placecommander.com multidomains certificate.

**WARING** As stated here
http://msdn.microsoft.com/en-us/library/windows/apps/ff941099(v=vs.105).aspx the Root Certificate Authority (CA) of the certificate must be one of the CAs listed at: SSL Root Certificates for Windows Phone, TLS and The Key-Usage value of the TLS certificate must be set to include client authentication.




openssl x509 -in certificate.crt -text -noout
            ……….
            X509v3 Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication  #
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            …….
~~~


To upload a Transport Layer Security (TLS) certificate to your account on Dev Center you must use th. When you upload the certificate the  "servicename" must be filled with the "commonname" of the  CSR we used to create the certificate ( "placecommander.com" ):

The certificate and budle can be dowloaded from godaddy(select apace) or FunGoStudiosWallet

* 27d939a6372a79.crt
* gd_bundle.crt

We need to upload only 27d939a6372a79.crt not the intermediate certificate gd_bundle.crt:  https://dev.windowsphone.com/ -> Dashboard -> Account -> MPN Certificates

FunGoStudiosWallet/fungostudios.com_ssl_cert/ssl_cert_private_key_fungostudios.com.tgz.gpg contains:

* `server.csr` the certificate signing request
* `server.key` the password protected private key
* `server.key.insecure` the not password protected private key

NB: Your web service initially is authenticated for four months after the certificate is uploaded. When you’re finished developing your app, submit it to Dev Center and make sure to select the appropriate TLS certificate during submission. When your app passes certification and is published on Dev Center, the four-month authentication limit will be removed.


To send:

~~~

openssl x509 -in fungostudios.com.crt -out fungostudios_cert_only.pem -outform PEM
openssl x509 -in gd_bundle.crt  -out gd_bundle.pem -outform PEM
cat server.key.insecure >> all.pem
cat fungostudios_cert_only.pem >> all.pem
cat gd_bundle.pem >> all.pem

curl --cert all.pem -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://am3.notify.live.net/throttledthirdparty/01.00/AQGt7RVZch7mRJ6czaulIGXIAgAAAAADIQAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQFBlVTTkMwMQ -v

curl --cert gd_bundle.pem --cert 27d939a6372a79.pem --key server.key.insecure  -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://db3.notify.live.net/unthrottledthirdparty/01.00/AQGt7RVZch7mRJ6czaulIGXIAgAAAAADIgAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQFBlVTTkMwMQ -v

curl -k  --cert all.pem  --key server.key.insecure  -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://db3.notify.live.net/unthrottledthirdparty/01.00/AQGt7RVZch7mRJ6czaulIGXIAgAAAAADIgAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQFBlVTTkMwMQ -v

curl -k --key server.key.insecure --cert server.csr --cacert gd_bundle.crt -v  -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://db3.notify.live.net/unthrottledthirdparty/01.00/AQGt7RVZch7mRJ6czaulIGXIAgAAAAADIgAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQFBlVTTkMwMQ -v

curl --key server.key.insecure --cert server.csr --cacert gd_bundle.crt -v  -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://db3.notify.live.net/unthrottledthirdparty/01.00/AQGt7RVZch7mRJ6czaulIGXIAgAAAAADIgAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQFBlVTTkMwMQ -v

~~~

The Push notification format is described here: http://msdn.microsoft.com/en-us/library/windowsphone/develop/hh202945%28v=vs.105%29.aspx

To ask for throttledthirdparty:

~~~
HttpNotificationChannel("mychannel")
~~~

To ask for an "unthrottled" certificate, you can use the Common Name of one of your certificates registered into the portal:

~~~
HttpNotificationChannel("mychannel","*.fungostudios.com")
~~~

Server implementation:

* A production server should work only with https channels, we should check that the uri provided is https. An http channel contains "throttledthirdparty" in the url, and https contains "unthrottled".
* If a client sends you http throttledthirdparty channel you cannot change the protocol, you must require an unthrottled channel.
    you can send only 1 notification per post request


the MSDN return 403 http://answers.flyppdevportal.com/categories/winphone/wpnotifications.aspx?ID=6b449d16-0bf4-4d20-af5a-8d60f3814185


non capisco perchè se metto HttpNotificationChannel("mychannel","shakechat.com") nell'app mi torna un uri https

mentre se metto HttpNotificationChannel("mychannel","*.fungostudios.com") mi torna un http..... boh

NB: con http c'è la parola throttled mentre con https c'è scritto unthrottled, you cannot simply change the protocol, the client must provide you the proper URI, if not you need to fix you application code or the app configuration on the Dev Center.

* TODO: Add a check server side to Tregg and show a developer alert if you app is using a http
* TODO: Define a policy for http uri, they are not sure and could be abused

SOL: the problem was that the certificate was not associated with any application. You must set the exact common name that you set as common name for example "*.fungostudios.com"

~~~
openssl x509 -in 27d939a6372a79.crt -out 27d939a6372a79.pem -outform PEM
openssl x509 -in gd_bundle.crt -out gd_bundle.pem -outform PEM
~~~

See Here for details:
http://blogs.windows.com/windows_phone/b/wpdev/archive/2013/06/06/no-quota-push-notifications-using-a-root-certificate-authority.aspx


# TODO ripulire gli appunti qua sotto
Our Tregg server must use the "notification URI" returned by the Tregg-wp8. The "notification URI" must be updated each time the application starts.
The app should encrypt its notification channel URI before sending the URI to its corresponding cloud service ->> use https

The cloud service should validate the notification channel URI received from its corresponding app and store it in a secure manner.

The cloud service should have a status code that it can send to its corresponding app that will trigger the app to create a new notification channel URI: The Tregg server should validate the "notification URI" and return a proper status code to tregg-wp8.

TODO come si valida l'URI?


Tregg Server:
MS servise rest response code:
http://msdn.microsoft.com/en-us/library/windowsphone/develop/ff941100%28v=vs.105%29.aspx



~~~
Tregg Server:
Auth:
curl --cert client_cert.pem -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>"
http://sn1.notify.live.net/throttledthirdparty/01.00/AAFDkFBar2Q9SJDPN6J1037RAgAAAAADAQAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ

Not Auth Toast:
curl -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" http://sn1.notify.live.net/throttledthirdparty/01.00/AAEfe3yoI8F3RqsMfG-Ab1ULAgAAAAADAQAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ


curl -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" http://sn1.notify.live.net/throttledthirdparty/01.00/AAE5MCLeyAZ0Sr-ddYmsyV3SAgAAAAADAQAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ


curl  --cert fungostudios_cert_only.pem  -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://sn1.notify.live.net/unthrottledthirdparty/01.00/AAEPXUQ9CJpBQK489vLwH6fwAgAAAAADFwAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ

curl --cert all.pem  -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://sn1.notify.live.net/unthrottledthirdparty/01.00/AAEPXUQ9CJpBQK489vLwH6fwAgAAAAADFwAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ


~~~

NB: Note  that  --cert  option assumes  a  "certificate" file that is the private key and the private certificate concatenated! See --cert and --key to specify them inde-pendently.

~~~
curl --cert all.pem  -v -H "Content-Type:text/xml" -H "X-WindowsPhone-Target:Toast" -H "X-NotificationClass:2" -X POST -d "<?xml version='1.0' encoding='utf-8'?><wp:Notification xmlns:wp='WPNotification'><wp:Toast><wp:Text1>My title</wp:Text1><wp:Text2>My subtitle</wp:Text2></wp:Toast></wp:Notification>" https://sn1.notify.live.net/unthrottledthirdparty/01.00/AAEPXUQ9CJpBQK489vLwH6fwAgAAAAADFwAAAAQUZm52OkJCMjg1QTg1QkZDMkUxREQ
~~~

fungostudios_cert.pem has the private key and must not be shared with MS server, you have to add it your server that send API call for push notification to MPNS. TODO: show and example with ruby (see here http://blog.mjfnet.com/2012/03/19/windows-phone-push-notifications-frequently-asked-questions/)

Then go to you windows phone dev account. Go to accounts and upload you public crt certificate.
Go to you app, select "more options" and connect the app with the certificate.

server.key.insecure is the unencrypted version of your key
now you can use only the --cert option of curl without the --key



ruby code: https://github.com/nverinaud/ruby-mpns


to convert CRT into PEM (to test with curl)
http://stackoverflow.com/questions/4691699/how-to-convert-crt-to-pem

Urban Airship wp8 push forum:
https://support.urbanairship.com/customer/portal/questions/1100922-test-push-not-working
https://support.urbanairship.com/customer/portal/articles/818712-windows-8-and-windows-phone-8-beta-support-faq

useful ssl commands
http://www.sslshopper.com/article-most-common-openssl-commands.html

Se il certificato
NB: Urban-airship non gestisce l'invio di push su WP8 senza un certificato per questioni di sicurezza

WARNING: we must use the https version of the URI (add a check server side)

VERY USEFUL FAQ:
http://blog.mjfnet.com/2012/03/19/windows-phone-push-notifications-frequently-asked-questions/


TRegg-WP8
* register ErrorOccurred event handler callback of the HttpNotificationChannel object.
* Connect to facebook:
http://www.developer.nokia.com/Community/Wiki/Integrate_Facebook_to_Your_Windows_Phone_Application
http://www.developer.nokia.com/Community/Wiki/Twitter:_OAuth_1.0_Authentication_using_Hammock


VARIE:
ruby + wp8 push
http://stackoverflow.com/questions/16603814/connect-to-microsoft-push-notification-service-for-windows-phone-8-from-ruby




Per testare InApp
su W8 c'è u

wp8 per testare puoi usare la modalità beta
abilitare il liveid
carino per dare ai siti




Pacchetto con 6 mesi di commitment minimo
euro 400 mese per 15M di API call
Le API call addizionali costano euro 100 al mese ogni 5M di API call
Sono comprese 24 ore di assistenza per l'integrazione e consulenza sulla gamification (per voi è un soft limit, non stiamo a guarda la giornata in più o in meno in questa fase)
Il pricing sulle API call resta invariato dopo i primi 6 mesi

Pacchetto on demand
Nel caso che vogliate procedere on demand il prezzo delle API call resta invariato:
euro 400 mese per 15M di API call
Le API call addizionali costano euro 100 al mese ogni 5M di API call
La tariffa per consulenze sull'integrazione e consulenza sulla gamification è di 400 euro a giornata


La prima soluzione è più vantaggiosa nel caso siate sicuri di procedere per più mesi, mentre la seconda se volete fare una campagna di un paio di mesi è più conveniente.



WP8 Store TIPS
1) To complete an application submission go to: Dashboard -> "click the name of your app"-> Current submission -> Complete
   NB: sometime the wp8 site is broken and some button may not appear, retry later


