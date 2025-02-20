import json
from src.Protobuf.Message_pb2 import ApiToSubtitleTransformer, MediaPod, Video, Preset

class ProtobufConverter:
    @staticmethod
    def json_to_protobuf(message: str) -> ApiToSubtitleTransformer:
        data = json.loads(message)
        print(data)
        media_pod_data = data["mediaPod"]

        video = Video()
        video.name = media_pod_data["originalVideo"]["name"]
        video.mimeType = media_pod_data["originalVideo"]["mimeType"]
        video.size = int(media_pod_data["originalVideo"]["size"])
        video.subtitle = media_pod_data["originalVideo"]["subtitle"]
        video.audios.extend(media_pod_data["originalVideo"]["audios"])
        video.subtitles.extend(media_pod_data["originalVideo"]["subtitles"])

        video.IsInitialized()

        preset = Preset()
        preset.subtitleFont = media_pod_data["preset"]["subtitleFont"]
        preset.subtitleSize = media_pod_data["preset"]["subtitleSize"]
        preset.subtitleColor = media_pod_data["preset"]["subtitleColor"]
        preset.subtitleBold = media_pod_data["preset"]["subtitleBold"]
        preset.subtitleItalic = media_pod_data["preset"]["subtitleItalic"]
        preset.subtitleUnderline = media_pod_data["preset"]["subtitleUnderline"]
        preset.subtitleOutlineColor = media_pod_data["preset"]["subtitleOutlineColor"]
        preset.subtitleOutlineThickness = media_pod_data["preset"]["subtitleOutlineThickness"]
        preset.subtitleShadow = media_pod_data["preset"]["subtitleShadow"]
        preset.subtitleShadowColor = media_pod_data["preset"]["subtitleShadowColor"]

        preset.IsInitialized()
        
        media_pod = MediaPod()
        media_pod.uuid = media_pod_data["uuid"]
        media_pod.userUuid = media_pod_data["userUuid"]
        media_pod.status = media_pod_data["status"]
        media_pod.originalVideo.CopyFrom(video)
        media_pod.preset.CopyFrom(preset)

        media_pod.IsInitialized()

        proto_message = ApiToSubtitleTransformer()
        proto_message.mediaPod.CopyFrom(media_pod)

        proto_message.IsInitialized()

        return proto_message
