
# Parameters

    Name :                      Attempt2_Diamonds1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal2
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      49241868978 function calls (47653446998 primitive calls) in 258900.86 seconds

##    Ordered by: cumulative time
   List reduced from 426 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.857 258900.857 {built-in method builtins.exec}
                      1    0.387    0.387 258900.856 258900.856 <string>:1(<module>)
                      1 6247.016 6247.016 258900.469 258900.469 optionCritic.py:195(option_critic_run)
               56487250 9792.279    0.000 114794.011    0.002 optionCritic.py:143(actor_loss_fn)
        2097861371/516783248 10317.117    0.000 113167.841    0.000 module.py:866(_call_impl)
              175675347  865.913    0.000 105481.896    0.001 optionCritic.py:70(get_state)
              175675347 2271.262    0.000 101962.934    0.001 container.py:117(forward)
                2259490   19.414    0.000 72285.456    0.032 tensor.py:195(backward)
                2259490   24.270    0.000 72265.739    0.032 __init__.py:68(backward)
                2259490 72188.731    0.032 72188.731    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              351350694  983.583    0.000 63696.830    0.000 conv.py:398(forward)
              351350694  557.518    0.000 62283.762    0.000 conv.py:390(_conv_forward)
              351350694 61726.244    0.000 61726.244    0.000 {built-in method conv2d}
              692458595 1696.933    0.000 22191.490    0.000 linear.py:93(forward)
               56487250 3412.650    0.000 20052.820    0.000 optionCritic.py:91(get_action)
              692458595  675.963    0.000 19786.299    0.000 functional.py:1737(linear)
              692458595 18960.313    0.000 18960.313    0.000 {built-in method torch._C._nn.linear}
               56487250 1394.183    0.000 15673.944    0.000 optionCritic.py:80(predict_option_termination)
              112974500 1350.933    0.000 8369.537    0.000 distribution.py:34(__init__)
                2259490   52.359    0.000 8325.465    0.004 optimizer.py:84(wrapper)
                2259490   29.601    0.000 8133.050    0.004 grad_mode.py:24(decorate_context)
                2259490  131.659    0.000 8048.004    0.004 rmsprop.py:56(step)
                2259490  134.512    0.000 7768.268    0.003 _functional.py:203(rmsprop)
              527026041  532.187    0.000 7401.791    0.000 activation.py:713(forward)
              527026041  551.866    0.000 6869.604    0.000 functional.py:1364(leaky_relu)
               56487250  563.683    0.000 6677.922    0.000 categorical.py:115(log_prob)
               56487250  555.561    0.000 6566.754    0.000 bernoulli.py:34(__init__)
              527026041 6203.165    0.000 6203.165    0.000 {built-in method torch._C._nn.leaky_relu}
              171081279  390.265    0.000 5643.623    0.000 optionCritic.py:77(get_Q)
               56487250  762.161    0.000 5632.192    0.000 categorical.py:49(__init__)
                 564872   98.973    0.000 4792.131    0.008 optionCritic.py:116(critic_loss_fn)
              113539372  420.055    0.000 4542.639    0.000 optionCritic.py:88(get_terminations)
               31632854 3881.317    0.000 3881.317    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2259490   12.156    0.000 3528.869    0.002 game.py:42(step)
               56487250 2306.857    0.000 3419.189    0.000 constraints.py:398(check)
                2259490   21.440    0.000 3392.864    0.002 layers.py:827(step)
               56487250  467.673    0.000 2723.126    0.000 distribution.py:240(_validate_sample)
               31632854 2682.759    0.000 2682.759    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56487250  532.053    0.000 2408.247    0.000 bernoulli.py:86(sample)
               56487250 2347.426    0.000 2347.426    0.000 constraints.py:364(check)
              175675347  231.047    0.000 2106.361    0.000 activation.py:101(forward)
                2259490   84.873    0.000 1961.218    0.001 layers.py:17(step)
             2717670121 1907.215    0.000 1907.386    0.000 module.py:934(__getattr__)
              175675347  199.265    0.000 1875.313    0.000 functional.py:1195(relu)
               56487250  146.130    0.000 1869.028    0.000 layer.py:106(move)
               56487250  970.625    0.000 1840.598    0.000 categorical.py:123(entropy)
              395410750 1819.394    0.000 1819.394    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               56487250 1772.842    0.000 1772.842    0.000 constraints.py:249(check)
              169461750  223.391    0.000 1662.613    0.000 utils.py:106(__get__)
              112974500  599.562    0.000 1661.838    0.000 functional.py:46(broadcast_tensors)
              175675347  182.219    0.000 1655.558    0.000 flatten.py:39(forward)
              175675347 1647.926    0.000 1647.926    0.000 {built-in method relu}
              170591494  209.329    0.000 1644.519    0.000 tensor.py:525(__rsub__)
               56487250  366.765    0.000 1589.548    0.000 utils.py:11(broadcast_all)
              175675347 1473.339    0.000 1473.339    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               24854390   60.874    0.000 1452.543    0.000 tensor.py:575(__iter__)
              170591494 1405.766    0.000 1405.766    0.000 {built-in method rsub}
                2259491  195.950    0.000 1401.742    0.001 layers.py:793(update)
              113539372 1375.926    0.000 1375.926    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24854390 1357.965    0.000 1357.965    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56487250  371.363    0.000 1317.580    0.000 categorical.py:108(sample)
                 564872 1083.838    0.002 1311.812    0.002 replaybuffer.py:42(sample_option_critic)
              170026622 1259.387    0.000 1259.387    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               56487250   67.739    0.000 1258.912    0.000 categorical.py:88(logits)
             2122715761 1246.239    0.000 1246.239    0.000 {built-in method torch._C._get_tracing_state}
               56487250   75.890    0.000 1191.173    0.000 utils.py:82(probs_to_logits)
             9072976377 1139.307    0.000 1156.315    0.000 {built-in method builtins.len}
              169461750 1153.572    0.000 1153.572    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               56487250  241.263    0.000 1121.366    0.000 layers.py:844(check)
              169461750 1042.846    0.000 1042.846    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8567120831 1004.549    0.000 1004.549    0.000 {method 'values' of 'collections.OrderedDict' objects}
              112974500  893.364    0.000  893.364    0.000 {built-in method broadcast_tensors}
               56487250  854.232    0.000  854.232    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2259490   86.301    0.000  758.841    0.000 replaybuffer.py:34(save_option_critic)
               56487250  147.726    0.000  686.492    0.000 utils.py:77(clamp_probs)
               56487250  685.608    0.000  685.608    0.000 {built-in method bernoulli}
                2259490  108.468    0.000  679.940    0.000 optimizer.py:189(zero_grad)
              171156366  665.596    0.000  665.596    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56487250  574.045    0.000  574.045    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               56977035  571.510    0.000  571.510    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               56487250  538.766    0.000  538.766    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              340053244  535.783    0.000  535.783    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              745982963  330.909    0.000  512.817    0.000 {built-in method builtins.isinstance}
              112974500  484.143    0.000  484.143    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56487250  100.595    0.000  481.152    0.000 layers.py:838(isFree)
               56487250  460.042    0.000  460.042    0.000 {built-in method clamp}
              169956077  441.275    0.000  441.275    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               31632854  435.882    0.000  435.882    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15816437  262.885    0.000  434.466    0.000 layer.py:175(NoRock_update)
               56487250  428.791    0.000  428.791    0.000 {built-in method log}
               15251560  426.044    0.000  426.044    0.000 {built-in method tensor}
              169461775  145.598    0.000  415.651    0.000 {built-in method builtins.all}
               56487250  408.109    0.000  408.109    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              175675361  404.212    0.000  404.212    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              317062035  324.993    0.000  380.557    0.000 layer.py:103(isFree)
               31632854  372.686    0.000  372.686    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               56487250  367.544    0.000  367.544    0.000 {built-in method all}
               58746766  179.760    0.000  357.752    0.000 grad_mode.py:119(__enter__)
               56487250  347.563    0.000  347.563    0.000 {built-in method multinomial}
                6778474   16.817    0.000  328.753    0.000 game.py:38(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606118: <Attempt2_Diamonds1_option_critic_2> in cluster <dcc> Done

Job <Attempt2_Diamonds1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
Terminated at Thu May  6 01:28:27 2021
Results reported at Thu May  6 01:28:27 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258281.20 sec.
    Max Memory :                                 873 MB
    Average Memory :                             859.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15511.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258919 sec.

The output (if any) is above this job summary.

