
# Parameters

    Name :                      Attempt2_Monsters_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      51763922142 function calls (50170368587 primitive calls) in 258900.76 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.763 258900.763 {built-in method builtins.exec}
                      1    0.395    0.395 258900.763 258900.763 <string>:1(<module>)
                      1 6380.744 6380.744 258900.368 258900.368 optionCritic.py:195(option_critic_run)
               56669750 9730.390    0.000 114439.523    0.002 optionCritic.py:143(actor_loss_fn)
        2105508340/519322042 10368.141    0.000 112747.343    0.000 module.py:866(_call_impl)
              176242922  871.676    0.000 104905.511    0.001 optionCritic.py:70(get_state)
              176242922 2311.223    0.000 101421.964    0.001 container.py:117(forward)
                2266790   21.204    0.000 72445.988    0.032 tensor.py:195(backward)
                2266790   23.971    0.000 72424.466    0.032 __init__.py:68(backward)
                2266790 72344.833    0.032 72344.833    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              352485844  976.748    0.000 62634.232    0.000 conv.py:398(forward)
              352485844  619.189    0.000 61253.463    0.000 conv.py:390(_conv_forward)
              352485844 60634.274    0.000 60634.274    0.000 {built-in method conv2d}
              695564964 1649.128    0.000 22516.957    0.000 linear.py:93(forward)
               56669750 3530.232    0.000 20624.697    0.000 optionCritic.py:91(get_action)
              695564964  691.124    0.000 20149.500    0.000 functional.py:1737(linear)
              695564964 19314.762    0.000 19314.762    0.000 {built-in method torch._C._nn.linear}
               56669750 1297.819    0.000 14867.075    0.000 optionCritic.py:80(predict_option_termination)
              113339500 1286.275    0.000 8249.749    0.000 distribution.py:34(__init__)
              528728766  501.437    0.000 7582.487    0.000 activation.py:713(forward)
              528728766  538.784    0.000 7081.050    0.000 functional.py:1364(leaky_relu)
               56669750  576.950    0.000 6846.111    0.000 categorical.py:115(log_prob)
                2266790   52.431    0.000 6625.568    0.003 optimizer.py:84(wrapper)
              528728766 6436.838    0.000 6436.838    0.000 {built-in method torch._C._nn.leaky_relu}
                2266790   29.627    0.000 6431.008    0.003 grad_mode.py:24(decorate_context)
                2266790  132.791    0.000 6345.135    0.003 rmsprop.py:56(step)
                2266790  143.988    0.000 6066.563    0.003 _functional.py:203(rmsprop)
               56669750  500.926    0.000 6065.129    0.000 bernoulli.py:34(__init__)
               56669750  794.306    0.000 5802.170    0.000 categorical.py:49(__init__)
              172503173  387.659    0.000 5756.601    0.000 optionCritic.py:77(get_Q)
                2266790   13.232    0.000 5303.120    0.002 game.py:42(step)
                2266790   20.988    0.000 5146.635    0.002 layers.py:827(step)
                 566697   97.252    0.000 4682.168    0.008 optionCritic.py:116(critic_loss_fn)
              113906197  428.558    0.000 4602.888    0.000 optionCritic.py:88(get_terminations)
               56669750 2388.665    0.000 3541.114    0.000 constraints.py:398(check)
               31735054 2785.508    0.000 2785.508    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56669750  475.211    0.000 2771.808    0.000 distribution.py:240(_validate_sample)
                2266790   89.725    0.000 2666.722    0.001 layers.py:17(step)
               56669750  177.229    0.000 2566.661    0.000 layer.py:106(move)
                2266791  193.173    0.000 2450.428    0.001 layers.py:793(update)
               56669750 2231.228    0.000 2231.228    0.000 constraints.py:364(check)
               56669750  425.324    0.000 2190.499    0.000 bernoulli.py:86(sample)
              176242922  230.206    0.000 2128.555    0.000 activation.py:101(forward)
               31735054 1987.839    0.000 1987.839    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56669750  260.376    0.000 1932.788    0.000 layers.py:844(check)
              176242922  194.539    0.000 1898.349    0.000 functional.py:1195(relu)
             2729057889 1898.142    0.000 1898.312    0.000 module.py:934(__getattr__)
               56669750  979.646    0.000 1868.437    0.000 categorical.py:123(entropy)
               56669750 1805.806    0.000 1805.806    0.000 constraints.py:249(check)
              396688250 1760.296    0.000 1760.296    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              176242922  188.577    0.000 1699.406    0.000 flatten.py:39(forward)
              170009250  234.432    0.000 1696.718    0.000 utils.py:106(__get__)
              176242922 1675.739    0.000 1675.739    0.000 {built-in method relu}
              113339500  574.098    0.000 1618.369    0.000 functional.py:46(broadcast_tensors)
              171142644  199.716    0.000 1609.592    0.000 tensor.py:525(__rsub__)
              176242922 1510.829    0.000 1510.829    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               24934690   60.551    0.000 1477.226    0.000 tensor.py:575(__iter__)
               56669750  299.068    0.000 1424.232    0.000 utils.py:11(broadcast_all)
               24934690 1381.772    0.000 1381.772    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              171142644 1380.293    0.000 1380.293    0.000 {built-in method rsub}
                 566697 1122.825    0.002 1351.465    0.002 replaybuffer.py:42(sample_option_critic)
               56669750  376.038    0.000 1346.089    0.000 categorical.py:108(sample)
              113906197 1322.888    0.000 1322.888    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               56669750   68.964    0.000 1282.961    0.000 categorical.py:88(logits)
              170575947 1280.752    0.000 1280.752    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2130443030 1267.306    0.000 1267.306    0.000 {built-in method torch._C._get_tracing_state}
               56669750   72.993    0.000 1213.997    0.000 utils.py:82(probs_to_logits)
              170009250 1185.824    0.000 1185.824    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8878234057 1118.961    0.000 1135.693    0.000 {built-in method builtins.len}
               56669750  653.731    0.000 1125.168    0.000 layers.py:538(check)
                1360554   21.716    0.000 1038.216    0.001 layers.py:849(restart)
              170009250 1019.104    0.000 1019.104    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8598276282  999.391    0.000  999.391    0.000 {method 'values' of 'collections.OrderedDict' objects}
               56669750  902.590    0.000  902.590    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1360554   11.723    0.000  881.123    0.001 level.py:8(__init__)
              113339500  878.944    0.000  878.944    0.000 {built-in method broadcast_tensors}
                1360554  127.041    0.000  790.671    0.001 levels.py:428(generate)
                2266790   85.852    0.000  776.041    0.000 replaybuffer.py:34(save_option_critic)
                2266790  109.007    0.000  717.102    0.000 optimizer.py:189(zero_grad)
               56669750  147.419    0.000  701.181    0.000 utils.py:77(clamp_probs)
              171709341  659.979    0.000  659.979    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56669750  642.621    0.000  642.621    0.000 {built-in method bernoulli}
               56669750  596.976    0.000  596.976    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               56669750  553.762    0.000  553.762    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              341151894  547.729    0.000  547.729    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58030279  543.611    0.000  543.611    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                6802770   86.406    0.000  528.854    0.000 level.py:41(notUsed)
               13600746  345.675    0.000  520.272    0.000 layer.py:159(update)
               10846305  240.147    0.000  512.914    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              113339500  501.792    0.000  501.792    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56549589   58.398    0.000  488.391    0.000 {built-in method builtins.any}
              761998503  289.766    0.000  487.757    0.000 {built-in method builtins.isinstance}
               56669750  474.015    0.000  474.015    0.000 {built-in method clamp}
               31735054  465.233    0.000  465.233    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15300835  444.073    0.000  444.073    0.000 {built-in method tensor}
               56669750  439.823    0.000  439.823    0.000 {built-in method log}
              390885651  142.189    0.000  430.184    0.000 layers.py:809(<genexpr>)
               56669750  424.348    0.000  424.348    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              176242936  417.420    0.000  417.420    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              171374335  417.173    0.000  417.173    0.000 {method 'item' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 239, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606141: <Attempt2_Monsters_option_critic_1> in cluster <dcc> Exited

Job <Attempt2_Monsters_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:12 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:14 2021
Terminated at Thu May  6 01:28:34 2021
Results reported at Thu May  6 01:28:34 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258245.11 sec.
    Max Memory :                                 789 MB
    Average Memory :                             764.74 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15595.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258950 sec.
    Turnaround time :                            258922 sec.

The output (if any) is above this job summary.

