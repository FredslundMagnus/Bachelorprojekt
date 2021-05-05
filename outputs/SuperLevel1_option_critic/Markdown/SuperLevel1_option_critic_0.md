[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
    Failed actions chance :     0.0
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


      29064272155 function calls (28211618372 primitive calls) in 258900.69 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.685 258900.685 {built-in method builtins.exec}
                      1    0.314    0.314 258900.685 258900.685 <string>:1(<module>)
                      1 3114.170 3114.170 258900.371 258900.371 optionCritic.py:195(option_critic_run)
        1126002776/277291400 8488.000    0.000 106000.414    0.000 module.py:866(_call_impl)
               30321950 8163.202    0.000 99481.800    0.003 optionCritic.py:143(actor_loss_fn)
               94301264  614.407    0.000 98471.158    0.001 optionCritic.py:70(get_state)
               94301264 2263.093    0.000 95915.923    0.001 container.py:117(forward)
                1212878    9.289    0.000 84573.335    0.070 tensor.py:195(backward)
                1212878   11.562    0.000 84563.815    0.070 __init__.py:68(backward)
                1212878 84521.558    0.070 84521.558    0.070 {method 'run_backward' of 'torch._C._EngineBase' objects}
              188602528  756.721    0.000 64379.810    0.000 conv.py:398(forward)
              188602528  297.143    0.000 63342.103    0.000 conv.py:390(_conv_forward)
              188602528 63044.960    0.000 63044.960    0.000 {built-in method conv2d}
               30321950 3159.304    0.000 18740.959    0.001 optionCritic.py:91(get_action)
              371592664 1328.347    0.000 17919.742    0.000 linear.py:93(forward)
                1212878   27.273    0.000 16721.420    0.014 optimizer.py:84(wrapper)
                1212878   14.224    0.000 16615.136    0.014 grad_mode.py:24(decorate_context)
                1212878   84.292    0.000 16573.190    0.014 rmsprop.py:56(step)
                1212878  135.700    0.000 16397.426    0.014 _functional.py:203(rmsprop)
              371592664  486.959    0.000 16078.748    0.000 functional.py:1737(linear)
              371592664 15487.481    0.000 15487.481    0.000 {built-in method torch._C._nn.linear}
               16980286 13983.204    0.001 13983.204    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               30321950  993.567    0.000 10623.962    0.000 optionCritic.py:80(predict_option_termination)
                 303219   70.471    0.000 7332.624    0.024 optionCritic.py:116(critic_loss_fn)
               60643900  893.007    0.000 6885.141    0.000 distribution.py:34(__init__)
              282903792  412.576    0.000 6654.989    0.000 activation.py:713(forward)
              282903792  373.248    0.000 6242.414    0.000 functional.py:1364(leaky_relu)
               30321950  494.158    0.000 6136.569    0.000 categorical.py:115(log_prob)
              282903792 5791.927    0.000 5791.927    0.000 {built-in method torch._C._nn.leaky_relu}
               30321950  714.429    0.000 5511.461    0.000 categorical.py:49(__init__)
               91721067  360.944    0.000 5203.485    0.000 optionCritic.py:77(get_Q)
               60947119  366.963    0.000 4249.591    0.000 optionCritic.py:88(get_terminations)
                1212878    7.116    0.000 3973.628    0.003 game.py:41(step)
                1212878   11.115    0.000 3867.146    0.003 layers.py:718(step)
               30321950  237.095    0.000 3786.789    0.000 bernoulli.py:34(__init__)
               30321950 2293.006    0.000 3440.052    0.000 constraints.py:398(check)
                1212878   57.124    0.000 2854.139    0.002 layers.py:17(step)
               30321950  189.093    0.000 2792.904    0.000 layer.py:98(move)
               30321950  377.751    0.000 2599.690    0.000 distribution.py:240(_validate_sample)
               30321950  328.931    0.000 1976.076    0.000 layers.py:735(check)
               94301264  133.111    0.000 1858.846    0.000 activation.py:101(forward)
               30321950  891.744    0.000 1826.982    0.000 categorical.py:123(entropy)
               30321950 1762.091    0.000 1762.091    0.000 constraints.py:249(check)
               94301264  126.460    0.000 1725.735    0.000 functional.py:1195(relu)
               30321950 1666.430    0.000 1666.430    0.000 constraints.py:364(check)
               94301264 1577.252    0.000 1577.252    0.000 {built-in method relu}
             1139344434 1515.243    0.000 1515.243    0.000 {built-in method torch._C._get_tracing_state}
               90965850  180.190    0.000 1499.394    0.000 utils.py:106(__get__)
              212253650 1463.167    0.000 1463.167    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               30321950  266.937    0.000 1420.984    0.000 bernoulli.py:86(sample)
               91572288  151.898    0.000 1374.188    0.000 tensor.py:525(__rsub__)
             1458483421 1317.714    0.000 1317.839    0.000 module.py:934(__getattr__)
               94301264   94.671    0.000 1301.293    0.000 flatten.py:39(forward)
               90965850 1279.749    0.000 1279.749    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               16980286 1214.964    0.000 1214.964    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               94301264 1206.622    0.000 1206.622    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               91269069 1194.973    0.000 1194.973    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               91572288 1194.802    0.000 1194.802    0.000 {built-in method rsub}
               30321950   58.327    0.000 1188.362    0.000 categorical.py:88(logits)
               30321950  304.165    0.000 1173.132    0.000 categorical.py:108(sample)
               30321950   61.801    0.000 1130.035    0.000 utils.py:82(probs_to_logits)
               60643900  332.169    0.000 1019.017    0.000 functional.py:46(broadcast_tensors)
                1212879  118.846    0.000  997.026    0.001 layers.py:684(update)
               60947119  971.734    0.000  971.734    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               90965850  885.628    0.000  885.628    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               13341658   38.078    0.000  861.427    0.000 tensor.py:575(__iter__)
             5044667201  848.411    0.000  859.596    0.000 {built-in method builtins.len}
               13341658  794.244    0.000  794.244    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             4598312368  739.060    0.000  739.060    0.000 {method 'values' of 'collections.OrderedDict' objects}
               30321950  148.295    0.000  734.583    0.000 utils.py:11(broadcast_all)
               30321950  107.903    0.000  689.156    0.000 utils.py:77(clamp_probs)
               30321950  668.600    0.000  668.600    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               60643900  600.445    0.000  600.445    0.000 {built-in method broadcast_tensors}
                1212878   61.968    0.000  586.032    0.000 replaybuffer.py:34(save_option_critic)
               91875507  585.337    0.000  585.337    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               30321950  581.253    0.000  581.253    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                 303219  427.645    0.001  568.123    0.002 replaybuffer.py:42(sample_option_critic)
               30321950  556.319    0.000  556.319    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               30321950  126.533    0.000  522.087    0.000 layers.py:729(isFree)
              182538138  520.991    0.000  520.991    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               30321950  510.723    0.000  510.723    0.000 {built-in method clamp}
                9790103  237.548    0.000  498.601    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               60643900  486.678    0.000  486.678    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               30321950  366.672    0.000  484.609    0.000 layers.py:471(check)
               30470729  469.356    0.000  469.356    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               15767427  285.820    0.000  465.296    0.000 layer.py:151(update)
               30321950  440.748    0.000  440.748    0.000 {built-in method bernoulli}
                1212878   72.768    0.000  401.242    0.000 optimizer.py:189(zero_grad)
              337989070  309.165    0.000  395.555    0.000 layer.py:95(isFree)
               30321950  381.819    0.000  381.819    0.000 {built-in method all}
               30321950  379.078    0.000  379.078    0.000 {built-in method log}
               30321950  371.932    0.000  371.932    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               16980286  369.653    0.000  369.653    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16980286  364.219    0.000  364.219    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               16980286  329.686    0.000  329.686    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              885968086  227.682    0.000  328.538    0.000 enum.py:646(__hash__)
                8186929  316.033    0.000  316.033    0.000 {built-in method tensor}
               30321950  221.071    0.000  294.272    0.000 layers.py:77(check)
               30321950  280.592    0.000  280.592    0.000 {built-in method multinomial}
              400439098  175.353    0.000  271.086    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601869: <SuperLevel1_option_critic_0> in cluster <dcc> Done

Job <SuperLevel1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:13 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:15 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:15 2021
Terminated at Sun May  2 21:36:20 2021
Results reported at Sun May  2 21:36:20 2021

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

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258843.48 sec.
    Max Memory :                                 1332 MB
    Average Memory :                             1319.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15052.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258907 sec.

The output (if any) is above this job summary.

