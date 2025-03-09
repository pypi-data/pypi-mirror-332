import 'dart:convert';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:onesignal_flutter/onesignal_flutter.dart';

class FletOneSignalControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const FletOneSignalControl({
    super.key,
    required this.parent,
    required this.control,
    required this.backend,
  });

  @override
  State<FletOneSignalControl> createState() => _FletOneSignalControlState();
}

class _FletOneSignalControlState extends State<FletOneSignalControl>
    with FletStoreMixin {
  @override
  void initState() {
    super.initState();
    _initializeOneSignal();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _setupNotificationHandler();
  }

  void _initializeOneSignal() {
    // Acessa o atributo "settings" do controle como uma string JSON
    final settings = widget.control.attrString("settings", "{}")!;

    // Decodifica a string JSON para um Map<String, dynamic>
    Map<String, dynamic> settingsData;

    if (settings != "{}") {
      try {
        settingsData = jsonDecode(settings);
        final appId = settingsData["app_id"] ??
            "DEFAULT_APP_ID"; // Valor padrão caso app_id seja nulo
        // Inicializa o OneSignal com o appId
        OneSignal.initialize(appId);
      } catch (error) {
        debugPrint("Erro: $error");
        widget.backend
            .triggerControlEvent(widget.control.id, "error", error.toString());
      }
    }
  }

  //   /// Configura os listeners para eventos de notificação
  void _setupNotificationHandler() {
    // Configura o listener para notificações abertas
    OneSignal.Notifications.addClickListener((event) {
      try {
        debugPrint("Notifications-addClickListener");

        final jsonData = jsonEncode({
          "json_data": event.notification.jsonRepresentation(),
        });

        widget.backend.triggerControlEvent(
          widget.control.id,
          "notification_received",
          jsonData,
        );
      } catch (error) {
        debugPrint("Erro: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    // Configura o listener para notificações recebidas
    OneSignal.Notifications.addForegroundWillDisplayListener((event) {
      try {
        debugPrint("Notifications-addForegroundWillDisplayListener");
        // Força a exibição da notificação localmente no app
        // event
        //     .preventDefault(); // Impede que o OneSignal ignore a exibição padrão
        // OneSignal.Notifications.displayNotification(
        //     event.notification.notificationId);

        final jsonData = jsonEncode({
          "json_data": event.notification.jsonRepresentation(),
        });

        // Envia os dados da notificação recebida para o Flet
        widget.backend.triggerControlEvent(
            widget.control.id, "notification_opened", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    OneSignal.InAppMessages.addClickListener((event) async {
      try {
        debugPrint("InAppMessages-addClickListener");

        // Decodificando as representações JSON para Map
        var messageMap = jsonDecode(event.message.jsonRepresentation());
        var resultMap = jsonDecode(event.result.jsonRepresentation());

        final jsonData = jsonEncode({
          "json_data": {
            "message": messageMap,
            "result": resultMap,
          }
        });

        widget.backend.triggerControlEvent(
            widget.control.id, "click_in_app_messages", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    OneSignal.InAppMessages.addWillDisplayListener((event) async {
      try {
        debugPrint("InAppMessages-addWillDisplayListener");

        var messageMap = jsonDecode(event.message.jsonRepresentation());

        final jsonData = jsonEncode({
          "json_data": messageMap,
        });

        debugPrint("dataStr: $jsonData");

        widget.backend.triggerControlEvent(
            widget.control.id, "will_display_in_app_messages", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    OneSignal.InAppMessages.addDidDisplayListener((event) async {
      try {
        debugPrint("InAppMessages-addDidDisplayListener");

        var messageMap = jsonDecode(event.message.jsonRepresentation());

        final jsonData = jsonEncode({
          "json_data": messageMap,
        });

        debugPrint("dataStr: $jsonData");

        widget.backend.triggerControlEvent(
            widget.control.id, "did_display_in_app_messages", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    OneSignal.InAppMessages.addWillDismissListener((event) async {
      try {
        debugPrint("InAppMessages-addWillDismissListener");

        var messageMap = jsonDecode(event.message.jsonRepresentation());

        final jsonData = jsonEncode({
          "json_data": messageMap,
        });

        debugPrint("dataStr: $jsonData");

        widget.backend.triggerControlEvent(
            widget.control.id, "will_dismiss_in_app_messages", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });

    OneSignal.InAppMessages.addDidDismissListener((event) async {
      try {
        debugPrint("InAppMessages-addDidDismissListener");

        var messageMap = jsonDecode(event.message.jsonRepresentation());

        final jsonData = jsonEncode({
          "json_data": messageMap,
        });

        debugPrint("dataStr: $jsonData");

        widget.backend.triggerControlEvent(
            widget.control.id, "did_dismiss_in_app_messages", jsonData);
      } catch (error) {
        debugPrint("Error: $error");

        widget.backend.triggerControlEvent(
          widget.control.id,
          "error",
          error.toString(),
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    debugPrint(
        "OneSignal build: ${widget.control.id} (${widget.control.hashCode})");

    () async {
      widget.backend.subscribeMethods(widget.control.id,
          (methodName, args) async {
        try {
          switch (methodName) {
            case "get_onesignal_id":
              var result = await OneSignal.User.getOnesignalId() ??
                  "The OneSignal ID does not exist.";
              return result;

            case "get_external_user_id":
              var result = await OneSignal.User.getExternalId() ??
                  "The external user ID does not yet exist.";
              return result;

            case "login":
              var externalUserId = args["external_user_id"] ?? "";
              OneSignal.login(externalUserId);
              return null;

            case "logout":
              OneSignal.logout();
              return null;

            case "add_alias":
              String alias = args["alias"] ?? "";
              dynamic idAlias = args["id_alias"];
              OneSignal.User.addAlias(alias, idAlias);
              return null;

            case "remove_alias":
              String alias = args["alias"] ?? "";
              OneSignal.User.removeAlias(alias);
              return null;

            case "set_language":
              String language = args["language"] ?? "en";
              OneSignal.User.setLanguage(language);
              return null;

            case "consent_required":
              String dataStr =
                  args["data"]!; // O '!' assume que o valor nunca será nulo
              Map<String, dynamic> dataMap = json.decode(dataStr);
              bool consent = dataMap["consent"] as bool;
              OneSignal.consentRequired(consent);
              return null;

            case "request_permission":
              String dataStr =
                  args["data"]!; // O '!' assume que o valor nunca será nulo
              Map<String, dynamic> dataMap = json.decode(dataStr);
              bool fallbackToSettings = dataMap["fallback_to_settings"] as bool;
              OneSignal.Notifications.requestPermission(fallbackToSettings);
              return null;

            case "opt_in":
              OneSignal.User.pushSubscription.optIn();
              return null;

            case "opt_out":
              OneSignal.User.pushSubscription.optOut();
              return null;

            case "register_for_provisional_authorization":
              var result = await OneSignal.Notifications
                  .registerForProvisionalAuthorization(true);
              return result.toString();

            case "can_request_permission":
              var result = await OneSignal.Notifications.canRequest();
              return result.toString();

            case "remove_notification":
              int notificationId = args["notification_id"] as int;
              OneSignal.Notifications.removeNotification(notificationId);
              return null;

            case "remove_grouped_notifications":
              var notificationGroup = args["notification_group"] ?? "";
              OneSignal.Notifications.removeGroupedNotifications(
                  notificationGroup);
              return null;

            case "clear_all_notifications":
              OneSignal.Notifications.clearAll();
              return null;

            case "prevent_default":
              var notificationId = args["notification_id"] ?? "";
              OneSignal.Notifications.preventDefault(notificationId);
              return null;

            default:
              return null;
          }
        } catch (error, stackTrace) {
          debugPrint("Erro no método $methodName: $error\n$stackTrace");
          widget.backend.triggerControlEvent(
            widget.control.id,
            "error",
            error.toString(),
          );
          return error.toString();
        }
      });
    }();

    return const SizedBox.shrink();
  }
}
